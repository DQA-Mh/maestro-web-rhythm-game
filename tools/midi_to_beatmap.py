#!/usr/bin/env python3
"""Convert MIDI to Maestro beatmap JSON. Requires: pip install mido."""
import json,sys
import mido

def midi_to_beatmap(path,output_path):
    midi=mido.MidiFile(path);events=[];elapsed=0.0
    for message in midi:
        elapsed+=message.time
        if message.type=='note_on' and message.velocity>0: events.append({'time':round(elapsed,3),'direction':message.note%4})
    with open(output_path,'w',encoding='utf-8') as stream: json.dump(events,stream,indent=2)

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('Usage: python tools/midi_to_beatmap.py input.mid output.json')
    midi_to_beatmap(sys.argv[1],sys.argv[2])
