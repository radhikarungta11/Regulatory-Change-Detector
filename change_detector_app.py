import streamlit as st
import difflib
import json
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # default Ollama API

def call_llm_with_prompt(prompt):
    response = requests.post(OLLAMA_API_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })
    result = response.json()
    return result.get("response", "")

def analyze_change(change_text):
    prompt = f"""
You are an expert in regulatory compliance. Given the following updated regulatory text, analyze and return a JSON object with these keys:

- "change_summary": a short 1-line summary of what changed.
- "change_type": one of "New Requirement", "Clarification of Existing Requirement", "Deletion of Requirement", or "Minor Edit".
- "potential_impact": a short note on how this might affect internal SOPs.

Text:
\"\"\"
{change_text}
\"\"\"
JSON:
"""
    raw = call_llm_with_prompt(prompt)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "change_summary": "Could not parse LLM output.",
            "change_type": "Unknown",
            "potential_impact": "Check manually."
        }

def detect_changes(text_v1, text_v2):
    v1_lines = [p.strip() for p in text_v1.split('\n') if p.strip()]
    v2_lines = [p.strip() for p in text_v2.split('\n') if p.strip()]
    
    sm = difflib.SequenceMatcher(None, v1_lines, v2_lines)
    changes = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'replace':
            for a, b in zip(v1_lines[i1:i2], v2_lines[j1:j2]):
                changes.append(('Modified', b))
        elif tag == 'insert':
            for b in v2_lines[j1:j2]:
                changes.append(('Added', b))
        elif tag == 'delete':
            for a in v1_lines[i1:i2]:
                changes.append(('Deleted', a))
    
    return changes

def main():
    st.set_page_config(page_title="Regulatory Change Detector")
    st.title("📄 AI-Powered Regulatory Change Detector")

    file1 = st.file_uploader("Upload OLD version (text_v1.txt)", type="txt")
    file2 = st.file_uploader("Upload NEW version (text_v2.txt)", type="txt")

    if st.button("🔍 Analyze Changes") and file1 and file2:
        text_v1 = file1.read().decode("utf-8")
        text_v2 = file2.read().decode("utf-8")

        with st.spinner("Detecting changes..."):
            changes = detect_changes(text_v1, text_v2)

        for change_type, changed_text in changes:
            if change_type in ['Added', 'Modified']:
                analysis = analyze_change(changed_text)
            else:
                analysis = {
                    "change_summary": "Text removed from previous version.",
                    "change_type": "Deletion of Requirement",
                    "potential_impact": "Check if internal policy depends on removed clause."
                }

            with st.expander(f"{change_type} Section:"):
                st.markdown(f"**Change Summary:** {analysis['change_summary']}")
                st.markdown(f"**Change Type:** `{analysis['change_type']}`")
                st.markdown(f"**Potential Impact:** {analysis['potential_impact']}")
                st.code(changed_text)

if __name__ == "__main__":
    main()
