# Phase 9, performance pass

The render loop uses requestAnimationFrame, notes use object pooling, detection is capped at about 24fps, webcam input targets 640x480, and external art/audio are avoided in the demo.

Test on Chrome and Edge, including a lower-spec machine. Production work remains: replace placeholder art and tune real audio sync.