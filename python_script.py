import json
import csv
import glob
import re
import os

# --- 1. CONFIGURATION ---
OUTPUT_FILENAME = 'clean_sports_data.csv'

# Define your strict keywords here.
# These will ONLY match if they appear as whole words.
SPORTS_KEYWORDS = [
    # Cricket
    'cricket',
    # Football
    'football', 
    # Chess
    'chess','basketball'
]

# --- 2. HELPER FUNCTIONS ---

def extract_text(entry, file_type):
    """
    Smart extraction of text from different file formats.
    """
    text_buffer = ""
    
    # Handle Dictionary (JSONL lines)
    if isinstance(entry, dict):
        if 'instruction' in entry: text_buffer += entry['instruction'] + " "
        if 'context' in entry: text_buffer += entry['context'] + " "
        if 'text' in entry: text_buffer += entry['text'] + " "
        if 'input' in entry: text_buffer += entry['input'] + " "
        if 'prompt' in entry: text_buffer += entry['prompt'] + " "
        
    # Handle CSV Dictionary (from DictReader)
    elif file_type == 'csv':
        if 'act' in entry: text_buffer += entry['act'] + " "
        if 'prompt' in entry: text_buffer += entry['prompt'] + " "
        
    return text_buffer.strip()

def find_exact_matches(text, keywords):
    """
    Returns the first keyword found as an exact whole word match.
    Example: 'I love cricket' -> returns 'cricket'
    Example: 'I hear crickets' -> returns None
    """
    normalized_text = text.lower()
    
    for word in keywords:
        # Regex explanation:
        # \b  -> Start of word boundary
        # word -> The specific keyword
        # \b  -> End of word boundary
        pattern = r'\b' + re.escape(word) + r'\b'
        
        if re.search(pattern, normalized_text):
            return word # Return immediately on first match
            
    return None

# --- 3. MAIN EXECUTION ---

def main():
    rows_to_save = []
    
    # Find all source files
    all_files = glob.glob('*.jsonl') + glob.glob('*.csv')
    
    # Avoid reading our own output file if it already exists
    if OUTPUT_FILENAME in all_files:
        all_files.remove(OUTPUT_FILENAME)
        
    print(f"📂 Processing files: {all_files}")
    print(f"🔍 Looking for {len(SPORTS_KEYWORDS)} strict keywords...")
    print("-" * 50)

    total_found = 0

    for filename in all_files:
        print(f"Reading {filename}...", end=" ")
        file_matches = 0
        
        try:
            # --- PROCESS JSONL ---
            if filename.endswith('.jsonl'):
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        try:
                            entry = json.loads(line)
                            text = extract_text(entry, 'jsonl')
                            
                            # STRICT CHECK
                            matched_word = find_exact_matches(text, SPORTS_KEYWORDS)
                            
                            if matched_word:
                                rows_to_save.append({
                                    'Source_File': filename,
                                    'Matched_Keyword': matched_word,
                                    'Prompt_Text': text
                                })
                                file_matches += 1
                        except json.JSONDecodeError:
                            continue

            # --- PROCESS CSV ---
            elif filename.endswith('.csv'):
                with open(filename, 'r', encoding='utf-8', errors='replace') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        text = extract_text(row, 'csv')
                        
                        # STRICT CHECK
                        matched_word = find_exact_matches(text, SPORTS_KEYWORDS)
                        
                        if matched_word:
                            rows_to_save.append({
                                'Source_File': filename,
                                'Matched_Keyword': matched_word,
                                'Prompt_Text': text
                            })
                            file_matches += 1
                            
            print(f"✅ Found {file_matches}")
            total_found += file_matches

        except Exception as e:
            print(f"❌ Error: {e}")

    # --- 4. WRITE CLEAN CSV ---
    print("-" * 50)
    if total_found > 0:
        headers = ['Source_File', 'Matched_Keyword', 'Prompt_Text']
        
        with open(OUTPUT_FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows_to_save)
            
        print(f"🏆 SUCCESS! Found {total_found} prompts.")
        print(f"💾 Data saved to: {OUTPUT_FILENAME}")
        print("open this file in Excel to see exactly which keyword matched each prompt.")
    else:
        print("⚠️ No matches found. Check your input files or keyword list.")

if __name__ == "__main__":
    main()