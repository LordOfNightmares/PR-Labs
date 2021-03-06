<details>
<summary>Task</summary>
  
## UDP & Network Sniffers

Studierea comunicării aplicațiilor în rețea. Refers engineering-ul protocolului aplicației.
Implementarea clientului propriu conform protocolului existent.

### Prerequisites

- [Wireshark](https://www.wireshark.org/)
- Limbajul de programare: nu este restricționat. Însă să recomandă un limbaj dinamic cu REPL*.
- Cunoștințe despre: [modelul OSI](https://en.wikipedia.org/wiki/OSI_model) și IP

Note:
- Informație despre git și linkuri utile găsești în [procesul de sustinere](submission-process.md);

### Obiective

- Studierea protocolului de transport UDP și compararea acestuia cu TCP;
- Studierea metodelor de captare a datelor transmise prin rețea și analiza acestora;
- Elaborarea unei aplicații client care să lucreze cu o aplicație existentă.

## Sarcini

Aplicația care trebuie să o analizați este un chat rudimentar proiectat ca să lucreze între mai multe calculatoare aceleași rețele.

![chat screenshot](imgs/local-chat.png)

Aplicația poate fi descărcată pe link-urile de mai jos pentru următoare platforme:
- Linux [x86](examples/l6/localchat-0.1.0-i386.AppImage) / [x64](examples/l6/localchat-0.1.0-x86_64.AppImage) **testat** (download, make executable and run)
- [Windows](examples/l6/localchat 0.1.0.exe)
- [MacOS [x64]](examples/localchat-0.1.0-mac.zip)

Notă: Cea mai simplă metodă de a testa aplicația este să porniți 2+ instanțe a aplicației pe același calculator. Astfel e mai simplu de testat și analizat datele.


### Sarcina de bază (5 - 6)

Utilizînd 2-3 instanțe a aplicației și wireshark captați schimbul de date, analizați mesajele și descrieți într-un document protocolul aplicației.
Documentul trebuie să conțină:
- Descrierea structurii generale a mesajelor,
- Tipurile mesajelor,
- Ordinea/workflow-ul mesajelor

### Sarcini adiționale (+1 pentru fiecare sarcină)

- Descrieți care sunt neajunsurile protocolului și transportului aplicației. 
- Implementați o aplicație care adaugă un utilizator nou în chat-ul pornit,
- Implementați posibilitatea de a expedia/primi mesaje
- Descrieți cum poate fi combinat UDP și TCP pentru așa tip de aplicație, care ar fi motivul și avantajul unei astfel de abordări.

**Notă:** La moment, aplicația nu funcționează conform așteptărilor între calculatoare aceleași rețele. Instanțele aplicației pe același calculator, este metoda recomandată de testare.
</details>

# Laboratory work 6

Open wireshark and select the interface we will be tracking, the interface I use is vEthernet (windows). 
To make work easier close the browser and all applications that are using internet. 
Open the application and select username and hit enter.

Now we need to filter our packets, to do this type `udp` in filter box.
The perfect scenario is that you should have one UDP paket. 
If you have multiple packets and can't find the one you are searcing we will cheat a little and filter it by port. 
The application is using the 42424 port as receiving port for all packets, to filter by port use `tcp.port == 42424`. The following screen is our wireshark window with the packet sent by application.

![ScreenShot](png/message1.png)
![ScreenShot](png/message2.png)
## Now we will try to Decode from base64 what those packet messages that we recieved.
![ScreenShot](png/decode1.png)
![ScreenShot](png/decode2.png)

## Decoding after a message was transfered in between 2 users:

#### •Packet 1
**Decode1**: `MTUyNzcxODk1MjQwMHw1MDFiNWNhYi1kM2Q1LTRkNzMtOThmYy0wZWY4YTk0OTRlYzF8YTYwODQzZGUtNzI4Zi00ZjkzLTkxYTYtNmY1MDViODgwZGNlfGV6cDBlWEJsSURwamFHRjBMQ0E2ZEhoMElDSlVTR2x6SUdseklHNXZkQ0JxZFhOMElHRWdjMmx0Y0d4bElHMWxjM05oWjJVdUluMD0=`

**Decode2**: `1527718952400|501b5cab-d3d5-4d73-98fc-0ef8a9494ec1|a60843de-728f-4f93-91a6-6f505b880dce|ezp0eXBlIDpjaGF0LCA6dHh0ICJUSGlzIGlzIG5vdCBqdXN0IGEgc2ltcGxlIG1lc3NhZ2UuIn0=`

**Decoded** = `{:type :chat, :txt "THis is not just a simple message."}`
##
Here the `1527718952400` is time in milisecconds.

![ScreenShot](png/timemilisec.png)

The `501b5cab-d3d5-4d73-98fc-0ef8a9494ec1` and `a60843de-728f-4f93-91a6-6f505b880dce` are the USSID's of the users that are currently comunicating.
And the `ezp0eXBlIDpjaGF0LCA6dHh0ICJUSGlzIGlzIG5vdCBqdXN0IGEgc2ltcGxlIG1lc3NhZ2UuIn0=` is the encoded Base64 message that was used in the comunication.
##
#### •Packet 2
**Decode1**: `MTUyNzcxODk1MjQwMnxhNjA4NDNkZS03MjhmLTRmOTMtOTFhNi02ZjUwNWI4ODBkY2V8NTAxYjVjYWItZDNkNS00ZDczLTk4ZmMtMGVmOGE5NDk0ZWMxfGV6cDBlWEJsSURwa1pXeHBkbVZ5WldSOQ==`

**Decode2**: `1527718952402|a60843de-728f-4f93-91a6-6f505b880dce|501b5cab-d3d5-4d73-98fc-0ef8a9494ec1|ezp0eXBlIDpkZWxpdmVyZWR9`

**Decoded** = `{:type :delivered}`
## Here i try inspecting the packets i recieved at the step of creating a new user
#### •Packet 1
**Decode after the step of user creation**: `MTUyNzcyMzAzNTIzOXw2YjlhYjAxMy1mZDBhLTRlZjMtOTcwNS1kYmQ1ODUxNjllMTB8OmFsbHxlenAwZVhCbElEcHZibXhwYm1Vc0lEcDFjMlZ5Ym1GdFpTQWlhMnNpZlE9PQ==`

**Decoded**: `1527723035239|6b9ab013-fd0a-4ef3-9705-dbd585169e10|:all|ezp0eXBlIDpvbmxpbmUsIDp1c2VybmFtZSAia2sifQ==`

**message**: `{:type :online, :username "kk"}`
##
#### •Packet 2
**Decode after recieving online users currently**: `MTUyNzcyMzAzNTI0OXw1MDFiNWNhYi1kM2Q1LTRkNzMtOThmYy0wZWY4YTk0OTRlYzF8NmI5YWIwMTMtZmQwYS00ZWYzLTk3MDUtZGJkNTg1MTY5ZTEwfGV6cDBlWEJsSURwdmJteHBibVVzSURwMWMyVnlibUZ0WlNBaWJXRmpNaUo5`

**Decoded**: `1527723035249|501b5cab-d3d5-4d73-98fc-0ef8a9494ec1|6b9ab013-fd0a-4ef3-9705-dbd585169e10|ezp0eXBlIDpvbmxpbmUsIDp1c2VybmFtZSAibWFjMiJ9`

**message**: `{:type :online, :username "mac2"}`
## I will now try to create an user and send an message on his behalf to the mac2 using packet sender.
**Creating the user**: `{:type :online, :username "crazy potato"}`

**Ussid**: `e369b064-6463-11e8-adc0-fa7ae01bbebc`

**PreEncode**: `1527723035239|e369b064-6463-11e8-adc0-fa7ae01bbebc|:all|ezp0eXBlIDpvbmxpbmUsIDp1c2VybmFtZSAiY3JhenkgcG90YXRvIn0=`

**Encoded**: `MTUyNzcyMzAzNTIzOXxlNDFjZTBiOC02NDYyLTExZTgtYWRjMC1mYTdhZTAxYmJlYmN8OmFsbHxlenAwZVhCbElEcHZibXhwYm1Vc0lEcDFjMlZ5Ym1GdFpTQWlZM0poZW5rZ2NHOTBZWFJ2SW4wPQ==`

![ScreenShot](png/packetsend.png)
![ScreenShot](png/packetsend1.png)
### Sending his message to mac2 with ussid `501b5cab-d3d5-4d73-98fc-0ef8a9494ec1`:
**message**: `{:type :chat, :txt "This is a try on sending a message with packets"}`

**Encoded message**: `ezp0eXBlIDpjaGF0LCA6dHh0ICJUaGlzIGlzIGEgdHJ5IG9uIHNlbmRpbmcgYSBtZXNzYWdlIHdpdGggcGFja2V0cyJ9=`

**PreEncode**: `1527723035249|e369b064-6463-11e8-adc0-fa7ae01bbebc|501b5cab-d3d5-4d73-98fc-0ef8a9494ec1|ezp0eXBlIDpjaGF0LCA6dHh0ICJUaGlzIGlzIGEgdHJ5IG9uIHNlbmRpbmcgYSBtZXNzYWdlIHdpdGggcGFja2V0cyJ9=`

**Encoded**: `MTUyNzcyMzAzNTI0OXw1MDFiNWNhYi1kM2Q1LTRkNzMtOThmYy0wZWY4YTk0OTRlYzF8ZTM2OWIwNjQtNjQ2My0xMWU4LWFkYzAtZmE3YWUwMWJiZWJjfGV6cDBlWEJsSURwamFHRjBMQ0E2ZEhoMElDSlVhR2x6SUdseklHRWdkSEo1SUc5dUlITmxibVJwYm1jZ1lTQnRaWE56WVdkbElIZHBkR2dnY0dGamEyVjBjeUo5PQ==`

![ScreenShot](png/packetsend2.png)

If you have multiple users and register, you will observe that multiple packets are sent, this happens because after receiving this packet, the app broadcasts packets to all users that are active.


