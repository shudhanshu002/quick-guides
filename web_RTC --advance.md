# WebRTC (Web Real-Time Communication) — Complete Notes  // till rtc and srtp

> Short, revision-focused notes. Focus is on **what each component does**, not implementation steps.

---

## 1. RTC (Real-Time Communication)

**RTC (Real-Time Communication)** = communication between devices with very low latency.

It can carry:

- Audio
- Video
- Screen sharing
- Chat/data
- Game state
- Mouse movements
- File chunks
- Whiteboard events
- Sensor data

### Normal HTTP (Hypertext Transfer Protocol) vs RTC

```text
HTTP:
Client → Request → Server
Client ← Response ← Server

RTC:
Device A ⇄ Device B
     real-time media/data
```

Main goal:

```text
LOW LATENCY
```

Unlike video streaming:

```text
Streaming:
Download → Buffer → Play

RTC:
Capture → Encode → Send → Decode → Play
                  continuously
```

---

# 2. WebRTC (Web Real-Time Communication)

**WebRTC (Web Real-Time Communication)** is a browser technology used to build real-time audio, video, and data communication.

It is more than a video-call API.

Major parts:

```text
WebRTC
├── Media capture
├── Peer connection
├── Signaling
├── SDP (Session Description Protocol)
├── ICE (Interactive Connectivity Establishment)
├── RTP (Real-time Transport Protocol)
├── RTCP (Real-time Transport Control Protocol)
├── DTLS (Datagram Transport Layer Security)
├── SRTP (Secure Real-time Transport Protocol)
├── DataChannel
├── Codecs
├── Congestion control
├── Jitter handling
├── Packet-loss handling
├── Simulcast
├── SVC (Scalable Video Coding)
├── SFU (Selective Forwarding Unit)
├── MCU (Multipoint Control Unit)
└── Statistics/monitoring
```

---

# 3. Media Capture

The browser can capture:

```javascript
const stream = await navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
});
```

Flow:

```text
Camera → VideoTrack
Mic    → AudioTrack
             ↓
        MediaStream
```

### MediaStream

**MediaStream** = container for media tracks.

### MediaStreamTrack

**MediaStreamTrack** = actual audio or video track that can be transmitted.

Important:

```text
MediaStream
├── VideoTrack → sent
└── AudioTrack → sent
```

The individual **MediaStreamTrack** objects are what are added for transmission.

---

# 4. RTCPeerConnection (Real-Time Communication Peer Connection)

```javascript
const pc = new RTCPeerConnection();
```

**RTCPeerConnection** manages the WebRTC connection.

It handles:

- Sending media
- Receiving media
- Negotiation
- Codec handling
- Security
- Network connectivity
- Statistics
- Media transport

Mental model:

```text
RTCPeerConnection
├── Send
├── Receive
├── Negotiate
├── Secure
└── Monitor
```

---

# 5. Adding Media Tracks

```javascript
stream.getTracks().forEach(track => {
    pc.addTrack(track, stream);
});
```

After adding:

```text
RTCPeerConnection
├── Video sender
└── Audio sender
```

---

# 6. Offer / Answer

WebRTC uses **offer/answer negotiation**.

### Offer

```javascript
const offer = await pc.createOffer();
```

The offer describes:

- Audio
- Video
- Supported codecs
- Media configuration
- Connection information

### Answer

The other peer receives the offer and creates:

```javascript
const answer = await pc.createAnswer();
```

Then both peers set:

```text
A:
localDescription  = A
remoteDescription = B

B:
localDescription  = B
remoteDescription = A
```

Purpose:

```text
"What are we sending?"
"What can we receive?"
"Which codecs/configuration?"
"How should the media session work?"
```

---

# 7. SDP (Session Description Protocol)

**SDP (Session Description Protocol)** = metadata describing a communication session.

It does **not** contain the actual video.

It describes things such as:

- Audio/video sections
- Codecs
- Media directions
- Media configuration
- Connection-related information
- Security identity/fingerprint information

Example:

```text
m=audio
m=video
```

Conceptually:

```text
SDP
├── Audio
├── Video
├── Codecs
├── Direction
└── Session configuration
```

Common media directions:

```text
sendrecv  → send + receive
sendonly  → send only
recvonly  → receive only
inactive  → neither
```

---

# 8. Signaling

**Signaling** = exchange of information required to establish and manage the WebRTC session.

WebRTC does not define a specific signaling server.

Possible technologies:

- WebSocket
- Socket.IO
- HTTP (Hypertext Transfer Protocol)
- Firebase
- Redis-backed services

Signaling can exchange:

- Offer
- Answer
- ICE (Interactive Connectivity Establishment) candidates
- Room information
- Participant information
- Connection/reconnection information

```text
Browser A
    ↓
Signaling Server
    ↓
Browser B
```

Important:

```text
Signaling Server ≠ Media Server
```

The signaling server normally does **not** carry every video frame.

---

# 9. ICE (Interactive Connectivity Establishment)

**ICE (Interactive Connectivity Establishment)** = mechanism used to find a usable network path between endpoints.

It works with:

- Network candidates
- STUN (Session Traversal Utilities for NAT)
- TURN (Traversal Using Relays around NAT)

High-level:

```text
WebRTC
   ↓
ICE
   ↓
Find usable network path
```

---

# 10. Media Pipeline

Actual video flow:

```text
Camera
   ↓
Raw Frames
   ↓
Video Encoder
   ↓
Compressed Video
   ↓
RTP (Real-time Transport Protocol)
   ↓
SRTP (Secure Real-time Transport Protocol)
   ↓
Network
   ↓
SRTP
   ↓
RTP
   ↓
Video Decoder
   ↓
Frames
   ↓
<video>
```

Audio:

```text
Microphone
   ↓
Audio Processing
   ↓
Audio Encoder
   ↓
RTP (Real-time Transport Protocol)
   ↓
SRTP (Secure Real-time Transport Protocol)
   ↓
Network
   ↓
Audio Decoder
   ↓
Speaker
```

---

# 11. Video Encoding

Camera produces raw frames:

```text
Frame 1
Frame 2
Frame 3
Frame 4
...
```

Raw video is too large to send directly.

A codec compresses it.

Common codecs:

- VP8
- VP9
- H.264
- AV1

```text
Raw Frames
    ↓
Codec
    ↓
Compressed Bitstream
```

---

# 12. RTP (Real-time Transport Protocol)

**RTP (Real-time Transport Protocol)** carries real-time audio/video media.

```text
Compressed Media
      ↓
RTP
      ↓
Packets
```

Instead of sending one large video object:

```text
Video
 ↓
Packet 1
Packet 2
Packet 3
Packet 4
...
```

---

# 13. RTP Packet

Conceptually:

```text
┌────────────────────────────┐
│ RTP Header                 │
├────────────────────────────┤
│ Encoded Media Payload      │
└────────────────────────────┘
```

Important RTP header fields:

```text
RTP Header
├── Sequence Number
├── Timestamp
├── SSRC (Synchronization Source)
└── Payload Type
```

---

# 14. Sequence Number

**Sequence Number** identifies packet order.

Example:

```text
100
101
102
103
```

If receiver gets:

```text
100
101
103
```

It can detect:

```text
102 → missing
```

Used for:

- Packet ordering
- Packet-loss detection
- Duplicate detection

Mental model:

```text
Sequence Number = WHICH packet?
```

---

# 15. Timestamp

**Timestamp** represents the media timing associated with the RTP packet.

Example:

```text
Frame 1 → 0
Frame 2 → 33
Frame 3 → 66
Frame 4 → 99
```

Mental model:

```text
Timestamp = WHEN should this media play?
```

Difference:

```text
Sequence Number → packet ordering
Timestamp       → media timing
```

---

# 16. SSRC (Synchronization Source)

**SSRC (Synchronization Source)** identifies an RTP source.

Example:

```text
Camera       → SSRC 1111
Microphone   → SSRC 2222
Screen share → SSRC 3333
```

Packets may arrive mixed:

```text
Packet → SSRC 1111
Packet → SSRC 2222
Packet → SSRC 1111
Packet → SSRC 3333
```

Receiver can identify the source.

Important:

```text
SSRC ≠ User ID
SSRC ≠ IP address
SSRC ≠ Peer ID
```

Mental model:

```text
SSRC       = WHO produced it?
Sequence   = WHICH packet?
Timestamp  = WHEN should it play?
```

SSRC identifies an RTP synchronization source, not necessarily one physical device.

---

# 17. Payload Type

**Payload Type** indicates the negotiated media format/codec associated with the RTP payload.

Possible codecs:

- Opus
- VP8
- VP9
- H.264
- AV1

Mental model:

```text
Payload Type = WHAT media format?
```

---

# 18. RTP (Real-time Transport Protocol) vs RTCP (Real-time Transport Control Protocol)

### RTP (Real-time Transport Protocol)

Carries actual media:

```text
Audio
Video
```

### RTCP (Real-time Transport Control Protocol)

Carries control and feedback information.

Examples:

- Packet loss
- Timing
- Statistics
- Reception information
- Feedback for media adaptation

```text
RTP  → Media
RTCP → Feedback / Control
```

---

# 19. Packet Loss

Real-time communication cannot wait indefinitely for missing packets.

Example:

```text
1 2 3 4 [5 missing] 6 7 8
```

WebRTC may use:

- Retransmission when useful
- Codec error resilience
- Keyframe request
- Packet-loss concealment

Core trade-off:

```text
Reliability
     ↕
Low Latency
```

For real-time communication:

```text
Low Latency > Perfect Delivery
```

---

# 20. Keyframes

Video can contain:

```text
I → P → P → P → P
```

**I-frame** = independent/keyframe.

If important reference information is lost, the receiver may need a new keyframe.

```text
Receiver
   ↓
Request Keyframe
   ↓
Sender
   ↓
New Keyframe
   ↓
Receiver
```

---

# 21. Jitter

**Jitter** = variation in packet arrival timing.

Packets may arrive:

```text
Packet 1 → 20 ms
Packet 2 → 25 ms
Packet 3 → 40 ms
Packet 4 → 22 ms
```

A **jitter buffer** helps smooth these timing variations before playback.

---

# 22. Congestion Control

Network capacity changes continuously.

Example:

```text
10 Mbps
   ↓
5 Mbps
   ↓
2 Mbps
```

If the sender keeps sending too much:

```text
High bitrate
    ↓
Queue grows
    ↓
Delay increases
    ↓
Packet loss
    ↓
Video freezes
```

Congestion control measures network conditions and adapts sending.

It considers things such as:

- Packet loss
- Delay
- Bandwidth
- Feedback

Result:

```text
Bitrate changes
      ↓
Video quality changes
```

Example:

```text
1080p
  ↓
720p
  ↓
480p
```

---

# 23. TWCC (Transport-Wide Congestion Control)

**TWCC (Transport-Wide Congestion Control)** provides transport-level feedback that helps estimate network conditions.

Used for:

- Bandwidth estimation
- Congestion control
- Bitrate adaptation

Mental model:

```text
Network feedback
      ↓
Bandwidth estimation
      ↓
Congestion control
      ↓
Bitrate adaptation
```

---

# 24. RTCRtpSender (Real-time Communication RTP Sender)

**RTCRtpSender (Real-time Communication RTP Sender)** represents the RTP sender for a media transceiver.

It is associated with outgoing media.

```text
MediaTrack
   ↓
RTCRtpSender
   ↓
RTP
   ↓
Network
```

Useful for controlling outgoing media, such as:

- Sending a track
- Replacing a track
- Encoding parameters

---

# 25. RTCRtpReceiver (Real-time Communication RTP Receiver)

**RTCRtpReceiver (Real-time Communication RTP Receiver)** represents the receiving side of an RTP media section.

```text
Network
   ↓
RTP
   ↓
RTCRtpReceiver
   ↓
MediaTrack
```

---

# 26. RTCRtpTransceiver (Real-time Communication RTP Transceiver)

**RTCRtpTransceiver (Real-time Communication RTP Transceiver)** represents one negotiated media relationship/section.

Think:

```text
Transceiver = Media Lane / Media Slot
```

Example:

```text
PeerConnection
├── Audio Transceiver
├── Video Transceiver
└── Screen-share Transceiver
```

Each transceiver has:

```text
Transceiver
├── Sender
├── Receiver
└── Direction
```

Directions:

```text
sendrecv
recvonly
sendonly
inactive
```

Example:

```text
Audio → send + receive
Video → receive only
```

A transceiver maps conceptually to a negotiated SDP (Session Description Protocol) media section such as:

```text
m=audio
m=video
m=video
```

It is especially useful when receiving media before having a local track:

```javascript
pc.addTransceiver("video", {
    direction: "recvonly"
});
```

Mental model:

```text
PeerConnection
       ↓
Transceiver
       ↓
One negotiated media lane
       ↓
Sender + Receiver
```

---

# 27. MID (Media Identification)

**MID (Media Identification)** identifies a negotiated media section/transceiver.

Mental model:

```text
MID → Which media section?
```

Example:

```text
MID → audio
MID → video
```

---

# 28. RID (RTP Stream Identifier)

**RID (RTP Stream Identifier)** identifies an RTP encoding/layer, commonly used with simulcast.

Example:

```text
Video
├── high   → 1080p
├── medium → 720p
└── low    → 360p
```

Mental model:

```text
SSRC → RTP source
MID  → media section
RID  → encoding/layer
```

---

# 29. Simulcast

**Simulcast** = sending multiple quality versions of the same video at the same time.

Example:

```text
Camera
   ↓
Video Encoder
   ├── High   → 1080p
   ├── Medium → 720p
   └── Low    → 360p
```

Different receivers can receive different quality.

Useful in group calls and SFU (Selective Forwarding Unit) systems.

---

# 30. SVC (Scalable Video Coding)

**SVC (Scalable Video Coding)** = video encoding using multiple scalable layers.

Conceptually:

```text
Base Layer
     +
Enhancement Layer
     +
More Enhancement
```

Allows the system to adapt video quality based on receiver/network conditions.

---

# 31. DataChannel

**DataChannel** allows arbitrary application data to be sent over WebRTC.

It is not limited to audio/video.

Can carry:

- Chat messages
- Game state
- Mouse movement
- Whiteboard events
- File chunks
- Sensor data

```text
Application Data
      ↓
DataChannel
      ↓
WebRTC
      ↓
Peer
```

For WebRTC DataChannel security, **DTLS (Datagram Transport Layer Security)** protects the data-channel traffic.

---

# 32. DTLS (Datagram Transport Layer Security)

**DTLS (Datagram Transport Layer Security)** provides security during connection establishment.

It is used to establish/derive cryptographic material.

High-level:

```text
DTLS Handshake
      ↓
Keying Material
      ↓
SRTP (Secure Real-time Transport Protocol)
      ↓
Protect RTP Media
```

Cryptographic material includes, at a high level:

- Encryption keys
- Authentication keys
- Salts/initialization parameters
- Algorithm/security parameters

The peers do not simply send one secret key directly.

---

# 33. DTLS-SRTP (Datagram Transport Layer Security - Secure Real-time Transport Protocol)

For WebRTC media:

```text
DTLS
 ↓
Secure handshake + key derivation
 ↓
SRTP
 ↓
Protect RTP packets
```

Important:

```text
DTLS ≠ direct encryption of every video packet
```

Instead:

```text
DTLS → establishes/derives security material
SRTP → protects RTP media
```

---

# 34. SRTP (Secure Real-time Transport Protocol)

**SRTP (Secure Real-time Transport Protocol)** protects RTP media.

Media path:

```text
RTP
 ↓
SRTP
 ↓
Encrypted + Authenticated Media
 ↓
Network
```

Receiver:

```text
Network
 ↓
SRTP
 ↓
RTP
 ↓
Decoder
```

SRTP provides:

- Confidentiality
- Authentication
- Integrity

---

# 35. SRTCP (Secure Real-time Transport Control Protocol)

**SRTCP (Secure Real-time Transport Control Protocol)** is the secure form of RTCP (Real-time Transport Control Protocol).

```text
RTP  → SRTP
RTCP → SRTCP
```

Therefore:

```text
Media    → RTP → SRTP
Feedback → RTCP → SRTCP
```

---

# 36. Certificates and Fingerprints

WebRTC uses DTLS certificates/fingerprints to authenticate the DTLS connection.

Purpose:

```text
Verify the expected peer
      ↓
Prevent simple man-in-the-middle substitution
```

SDP (Session Description Protocol) carries information related to the DTLS identity/fingerprint.

---

# 37. Complete Security + Media Flow

```text
Connection Setup:

SDP
 ↓
ICE
 ↓
DTLS Handshake
 ↓
DTLS-SRTP Key Derivation
 ↓
SRTP Ready
```

Actual media:

```text
Camera
 ↓
Encoder
 ↓
RTP
 ↓
SRTP 🔐
 ↓
UDP
 ↓
Internet
 ↓
SRTP 🔓
 ↓
RTP
 ↓
Decoder
 ↓
Video
```

---

# 38. SFU (Selective Forwarding Unit)

**SFU (Selective Forwarding Unit)** forwards media streams without normally decoding every video stream into raw frames.

For a group call:

```text
          SFU
        /  |  \
       /   |   \
    Alice Bob  Charlie
```

Participants mainly send media to the SFU.

```text
Alice → SFU
Bob   → SFU
Charlie → SFU
```

SFU forwards the appropriate streams.

Advantages:

- Lower client upload than mesh
- Efficient group communication
- Can select quality/layers
- Can forward RTP packets without full media decoding

---

# 39. P2P (Peer-to-Peer)

**P2P (Peer-to-Peer)** means peers communicate directly when possible.

For two users:

```text
Alice ⇄ Bob
```

For N users, mesh connections grow approximately as:

```text
N(N - 1) / 2
```

This becomes expensive for larger calls.

---

# 40. MCU (Multipoint Control Unit)

**MCU (Multipoint Control Unit)** receives, processes, and mixes media.

Typical concept:

```text
Participants
     ↓
   MCU
     ↓
Decrypt
     ↓
Decode
     ↓
Mix/Process
     ↓
Encode
     ↓
Encrypt
     ↓
Participants
```

MCU generally requires much more media processing than an SFU.

---

# 41. SFU vs MCU

| Feature | SFU (Selective Forwarding Unit) | MCU (Multipoint Control Unit) |
|---|---|---|
| Main job | Forward media | Mix/process media |
| Decode every stream | Usually no | Generally yes |
| Encode output | Usually no | Yes |
| Server processing | Lower | Higher |
| Media flexibility | High | Lower |
| Typical use | Modern group calls | Media mixing/composition |

---

# 42. Active Speaker

**Active Speaker** = identifying who is currently speaking.

Can be used to:

- Highlight speaker
- Change layout
- Prioritize speaker video
- Reduce unnecessary media

Conceptually:

```text
Audio activity
      ↓
Active speaker detection
      ↓
UI/layout decision
```

---

# 43. getStats()

`getStats()` provides WebRTC connection/media statistics.

Useful metrics:

- Packet loss
- RTT (Round-Trip Time)
- Jitter
- Bitrate
- Frames
- Freeze rate
- Connection state
- Network statistics

Production systems use these statistics for:

```text
Client
 ↓
Telemetry
 ↓
Monitoring
 ↓
Dashboard / Alerts
```

---

# 44. QoE (Quality of Experience)

**QoE (Quality of Experience)** = how good the communication feels to the user.

Important indicators:

- Video freezes
- Audio problems
- Delay
- Packet loss
- Connection failures
- Quality changes
- Bitrate

Example:

```text
Packet loss ↑
RTT ↑
Jitter ↑
Freeze rate ↑
        ↓
Poor QoE
```

---

# 45. Screen Sharing

Screen sharing is another media source.

Conceptually:

```text
Screen
  ↓
Video Track
  ↓
RTCPeerConnection
  ↓
RTP
  ↓
SRTP
  ↓
Network
```

A call may have:

```text
Audio Transceiver
Video Transceiver
Screen-share Transceiver
```

---

# 46. Renegotiation

**Renegotiation** = updating the negotiated media session after changes.

Examples:

- Add camera
- Remove camera
- Add screen share
- Stop screen share
- Change media direction
- Add another media section

Conceptually:

```text
Existing Session
      ↓
Media Change
      ↓
New Offer/Answer
      ↓
Updated Session
```

---

# 47. Recording

Production WebRTC systems may add a recording service.

Possible architecture:

```text
Participants
     ↓
    SFU
     ↓
Recording Service
     ↓
Storage
```

Recording may involve:

- Individual tracks
- Composed streams
- Dedicated recording workers

---

# 48. Large Webinars

WebRTC works well for interactive participants.

For very large one-way audiences, a system may combine:

```text
WebRTC Ingest
      ↓
Media Infrastructure
      ↓
CDN (Content Delivery Network)
      ↓
Many Viewers
```

For interactive users:

```text
WebRTC
```

For massive distribution:

```text
WebRTC → Media Infrastructure → CDN
```

---

# 49. WebRTC System Design

## 1:1 Call

```text
Alice
  │
  │ Signaling
  ↓
Signaling Server
  ↑
  │
  │ Signaling
  │
Bob

Alice ⇄ Bob
    WebRTC Media
```

Signaling handles:

- Offer
- Answer
- ICE candidates
- Room/session information

Media can travel directly between peers when the network path allows.

---

# 50. Group Call with SFU

```text
             SFU
          /   |   \
         /    |    \
      Alice  Bob  Charlie
```

Each participant primarily uploads once:

```text
Alice → SFU
```

SFU forwards streams:

```text
SFU → Bob
SFU → Charlie
```

---

# 51. Production Architecture

```text
                    Clients
                       │
                Load Balancer
                       │
              ┌────────┴────────┐
              ↓                 ↓
       Signaling/API        SFU Cluster
              │                 │
              │                 ├── Media Routing
              │                 ├── Layer Selection
              │                 └── Bandwidth Adaptation
              │
        Room / Session
              │
              ↓
        Room Management

Additional Services:
├── TURN (Traversal Using Relays around NAT)
├── Recording
├── Storage
├── Monitoring
└── Telemetry
```

---

# 52. Room Management

A production system needs:

- Room creation
- Room joining
- Room leaving
- Participant state
- Authentication
- Session management
- SFU assignment
- Reconnection

Example:

```text
Room
├── Room ID
├── Participants
├── SFU assignment
└── Session state
```

---

# 53. SFU Scaling

Do not put every room on one SFU.

```text
Room Router
     │
 ┌───┼────┐
 ↓   ↓    ↓
SFU1 SFU2 SFU3
```

Example:

```text
Room A → SFU1
Room B → SFU1
Room C → SFU2
Room D → SFU3
```

This is room-level scaling.

---

# 54. SFU Cluster

For large systems:

```text
Users
  ↓
Load Balancer
  ↓
Room Router
  ↓
SFU Cluster
```

The system considers:

- CPU
- Bandwidth
- Number of rooms
- Number of participants
- Regional capacity
- Network conditions

---

# 55. Multi-Region Architecture

**Multi-region** = running infrastructure in multiple geographic regions.

Conceptually:

```text
Users
  ↓
Global Routing
  ├── Region A → SFU Cluster
  ├── Region B → SFU Cluster
  └── Region C → SFU Cluster
```

Goals:

- Lower latency
- Better availability
- Regional failure handling
- Capacity distribution

---

# 56. Failure Handling

### SFU failure

```text
SFU failure
    ↓
Detect failure
    ↓
Reassign / Reconnect
    ↓
New SFU
    ↓
Renegotiate / Re-establish media
```

### Signaling failure

Signaling and media are separate paths.

Existing media may potentially continue even if signaling temporarily fails.

However:

- New negotiation may fail
- Reconnection may be affected
- New participants may not join

---

# 57. TURN (Traversal Using Relays around NAT)

**TURN (Traversal Using Relays around NAT)** provides a relay when a suitable direct path cannot be established.

Conceptually:

```text
Client
  ↓
TURN
  ↓
SFU / Peer
```

Direct path:

```text
Client ─────────→ SFU
```

Relay path:

```text
Client → TURN → SFU
```

TURN consumes relay bandwidth, so it is generally preferred as a fallback rather than the ideal path.

---

# 58. Monitoring

Production systems monitor:

- Packet loss
- RTT (Round-Trip Time)
- Jitter
- Bitrate
- Freeze rate
- Connection failures
- TURN usage
- SFU CPU
- SFU bandwidth
- QoE (Quality of Experience)

```text
Clients
   ↓
Statistics
   ↓
Telemetry
   ↓
Monitoring
   ↓
Dashboards + Alerts
```

Example:

```text
SFU CPU = 92%
Bandwidth = 18 Gbps
Packet loss = increasing
```

The system may stop assigning new rooms to an overloaded SFU.

---

# 59. Complete WebRTC Mental Model

```text
                         WebRTC
                            │
       ┌────────────────────┼────────────────────┐
       ↓                    ↓                    ↓
    Capture             Signaling             Security
       │                    │                    │
 Camera / Mic          SDP / ICE             DTLS-SRTP
       │
       ↓
    MediaTrack
       ↓
RTCPeerConnection
       ↓
 Transceiver
   ┌───┴────┐
   ↓        ↓
Sender   Receiver
   ↓
Encoder
   ↓
RTP
   ↓
SRTP
   ↓
Network
   ↓
SRTP
   ↓
RTP
   ↓
Decoder
   ↓
Audio / Video
```

---

# 60. Full 1:1 WebRTC Flow

```text
USER A

Camera + Mic
     ↓
MediaStream
     ↓
MediaStreamTrack
     ↓
RTCPeerConnection
     ↓
addTrack()
     ↓
createOffer()
     ↓
SDP
     ↓
Signaling
     ↓
USER B

setRemoteDescription()
     ↓
createAnswer()
     ↓
setLocalDescription()
     ↓
Signaling
     ↓
USER A

setRemoteDescription()
     ↓
Negotiation
     ↓
ICE
     ↓
DTLS Handshake
     ↓
SRTP Ready
     ↓
Media Transmission
```

Actual media:

```text
Camera
 ↓
Raw Frame
 ↓
Encoder
 ↓
RTP
 ↓
SRTP 🔐
 ↓
UDP (User Datagram Protocol)
 ↓
Internet
 ↓
SRTP 🔓
 ↓
RTP
 ↓
Decoder
 ↓
Video
```

---

# 61. Full Group Call Flow

```text
Participants
      │
      ↓
Signaling
      │
      ↓
Room Management
      │
      ↓
SFU
      │
      ├── Alice
      ├── Bob
      ├── Charlie
      └── Dave
```

Media:

```text
Alice → SFU
Bob → SFU
Charlie → SFU
Dave → SFU
```

SFU forwards appropriate media to each participant.

---

# 62. Core Differences to Remember

### Signaling vs Media

```text
Signaling
→ Offer
→ Answer
→ ICE candidates
→ Session information

Media
→ Audio
→ Video
→ RTP
→ SRTP
```

### RTP vs RTCP

```text
RTP  → Actual media
RTCP → Feedback/control
```

### DTLS vs SRTP

```text
DTLS → Secure handshake + key derivation
SRTP → Protects RTP media
```

### P2P vs SFU

```text
P2P → Peers communicate directly
SFU → Server forwards media
```

### SFU vs MCU

```text
SFU → Mostly forward
MCU → Decode + process/mix + encode
```

### SSRC vs MID vs RID

```text
SSRC → RTP synchronization source
MID  → Media section
RID  → RTP encoding/layer
```

### Sequence Number vs Timestamp

```text
Sequence Number → Packet order
Timestamp       → Media timing
```

---

# 63. WebRTC at Scale

A Zoom/Google Meet-like architecture can look like:

```text
                         Clients
                            │
                     Global Routing
                            │
                     Load Balancer
                            │
             ┌──────────────┴──────────────┐
             ↓                             ↓
       API / Signaling                 SFU Cluster
             │                             │
       Room Management              Media Routing
             │                             │
             │                  ┌──────────┼──────────┐
             │                  ↓          ↓          ↓
             │                 SFU1       SFU2       SFU3
             │
       ┌─────┴────────────────────────────────────┐
       ↓                 ↓            ↓           ↓
     TURN             Recording    Storage    Monitoring
```

For huge events:

```text
Interactive Users
      ↓
WebRTC
      ↓
SFU / Media Infrastructure
      ↓
CDN (Content Delivery Network)
      ↓
Massive Audience
```

---

# 64. WebRTC Quick Revision

```text
RTC (Real-Time Communication)
→ Low-latency communication

WebRTC (Web Real-Time Communication)
→ Browser technology for RTC

MediaStream
→ Container of media tracks

MediaStreamTrack
→ Actual audio/video track

RTCPeerConnection
→ Manages WebRTC connection

Transceiver
→ One negotiated media lane

Sender
→ Sends media

Receiver
→ Receives media

SDP (Session Description Protocol)
→ Session metadata

Signaling
→ Exchanges negotiation information

ICE (Interactive Connectivity Establishment)
→ Finds usable network path

RTP (Real-time Transport Protocol)
→ Carries media

RTCP (Real-time Transport Control Protocol)
→ Feedback/control

SSRC (Synchronization Source)
→ Identifies RTP source

Sequence Number
→ Packet order

Timestamp
→ Media timing

Payload Type
→ Media format/codec

DTLS (Datagram Transport Layer Security)
→ Secure handshake/key derivation

SRTP (Secure Real-time Transport Protocol)
→ Protects RTP media

SRTCP (Secure Real-time Transport Control Protocol)
→ Protects RTCP

DataChannel
→ Arbitrary real-time data

Simulcast
→ Multiple quality versions

SVC (Scalable Video Coding)
→ Scalable video layers

SFU (Selective Forwarding Unit)
→ Forwards media

MCU (Multipoint Control Unit)
→ Mixes/processes media

P2P (Peer-to-Peer)
→ Direct peer communication

TWCC (Transport-Wide Congestion Control)
→ Network feedback for congestion control

RTT (Round-Trip Time)
→ Time for a round trip

QoE (Quality of Experience)
→ User-perceived communication quality

CDN (Content Delivery Network)
→ Large-scale content distribution

TURN (Traversal Using Relays around NAT)
→ Relay when direct connectivity fails
```

---

# 65. One-Line Interview Mental Model

> **WebRTC is a low-latency communication system where signaling negotiates the session, ICE establishes connectivity, DTLS (Datagram Transport Layer Security) establishes security/keying, RTP (Real-time Transport Protocol) carries media, SRTP (Secure Real-time Transport Protocol) protects it, RTCP (Real-time Transport Control Protocol) provides feedback, and SFU (Selective Forwarding Unit) enables scalable group communication.**

---

## Source Scope

These notes combine and condense the two provided WebRTC/RTC study documents, preserving their main terminology and progression while removing repeated explanations and process-heavy detail.
