import pexpect
import cf_manager
import sys
import pyte




def run(network, device, prompt, command, logout):
    """Connect to a device, issue a command, and display the result"""
    session = pexpect.spawn("ssh user@host"
                            f"-- --network {network} --network_element {device}",
                            timeout=120)
    print(f"Connected to {device} on {network}.")
    print("\n")
    session.logfile = sys.stdout.buffer
    session.expect(prompt)
    session.send(command)
    capture = session.before
    screen = pyte.Screen(80, 24)
    stream = pyte.ByteStream(screen)
    stream.feed(capture)
    for line in screen.buffer:
        print(line)

    print(f"Disconnecting from the {network} network.")
    session.close()

if __name__ == "__main__":
    manager = cf_manager.get_manager()
    run(manager ,script_metadata_network,
        manager.script_metadata.device,
        manager.script_metadata.parameters['prompt'],
        manager.script_metadata.parameters['command'],
        manager.script_metadata.parameters['logout'])
