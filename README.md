# Peer-to-Peer Cue System #

Cue system for simple two-way communication and visual signaling using a WebRTC peer-to-peer connection.
This was initially designed for signaling on-stage actors during a theater performance.

Demo: [http://jackmckernan.tk/open-development/peer-to-peer-cue-system/](http://jackmckernan.tk/open-development/peer-to-peer-cue-system/)

[PeerJS examples](https://peerjs.com/examples)

### Setup ###

1. Open receive.html on the receiving device.
2. Open send.html on the sending device.
3. Copy the ID from the receiving device to the sending device's ID field.
4. Press *Connect*.
4. Both should indicate a successful connection in the *Status* box.

### Features ###

The receiver has access to large indicators for standby, go, fade, and stop signals. 

The sender has access to buttons that send the standby, go, fade, and stop signals, triggering the receiver's indicators.

Both have access to a two-way messenger for additional communication.


### Contact ###

Jack McKernan [jmcker@outlook.com](mailto:jmcker@outlook.com)
