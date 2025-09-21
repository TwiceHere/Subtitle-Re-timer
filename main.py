import utilities as ut
import argparse




def main(): 
    parser = argparse.ArgumentParser(description="subtitle retimer tool") 

    # shift flag 
    parser.add_argument(
        "-s", "--shift", 
        type=int, 
        required=True, 
        help="Shift time in milliseconds (can be negative)" 
    )
    parser.add_argument(
        "-i", "--inline",
        action = "store_true"
    )
    parser.add_argument(
        "filepath", 
        help="Path to subtitle file (.srt)" 
    )
    args = parser.parse_args()
    filepath = args.filepath
    shift = args.shift 
    with open(filepath,'r',encoding='utf-8') as f: 
        contents = f.read().strip()
    blocks,timestamps = ut.sub_to_blocks(contents) 

    for block in blocks: 
        block.shift(shift)

    updated_content = ut.update_sub(contents,blocks,timestamps)
    if args.inline: 
        with open(filepath,'w') as f: 
            f.write(updated_content) 
            print(f"Updated {filepath} with {shift} shift")
    else: 
        with open("updated" + filepath,'w') as f: 
            f.write(updated_content)
            print(f"Created {'updated' + filepath} with {shift} shift")

if __name__ == "__main__": 
    main()
