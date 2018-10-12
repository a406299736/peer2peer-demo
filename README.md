# peer2peer demo#

demo for simple two-way communication and visual signaling using a WebRTC peer 2 peer connection.
This was initially designed for signaling on-stage actors during a theater performance.

[PeerJS examples](https://peerjs.com/examples)

### Setup ###
You need install python3+, pip3, flask ...
Run python index.py

1. Click receive on the receiving device.
2. Click send on the sending device.
3. Copy the ID from the receiving device to the sending device's ID field.
4. Press *Connect*.
4. Both should indicate a successful connection in the *Status* box.

### Features ###

The receiver has access to large indicators for standby, go, fade, and stop signals. 

The sender has access to buttons that send the standby, go, fade, and stop signals, triggering the receiver's indicators.

Both have access to a two-way messenger for additional communication.

