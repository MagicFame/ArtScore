import sys
from mido import MidiFile

if __name__ == '__main__':
    filename = sys.argv[1]

    midi_file = MidiFile('haydn.mid')

    for i, track in enumerate(midi_file.tracks):
        sys.stdout.write('=== Track {}\n'.format(i))
        for message in track:
            sys.stdout.write('  {!r}\n'.format(message))