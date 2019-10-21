import sys,os
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new_note', action='store_true')
    parser.add_argument('-f', '--file', action='store_true')
    parser.add_argument('note', type=str, nargs='+')
    args = parser.parse_args()

    sticky_loc = '/home/tim/Desktop/notes/current_note.txt'
    if args.new_note:
        file_mode = 'w'
        if args.file:
            desc = input('Desired filename: ')
            fname = desc + '.txt'
        else: 
            now = datetime.datetime.now()
            fname = 'note_' + now.strftime("%m-%d-%Y-%H:%M") + '.txt'
        with open(sticky_loc) as f:
            with open(f'/home/tim/Desktop/notes/archive/{fname}', "w") as f1:
                for line in f:
                    f1.write(line)
    else:
        file_mode = 'a'
    note = ' '
    note = note.join(args.note)
    with open(sticky_loc, file_mode) as file:
        file.write(note + '\n\n')


if __name__ == '__main__':
    main()
