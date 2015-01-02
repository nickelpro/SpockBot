from spock.plugins.core import event, net, auth
from spock.plugins.helpers import start, keepalive, clientinfo, world, move, respawn

DefaultPlugins = [
	event.EventPlugin,
	net.NetPlugin,
	auth.AuthPlugin,
	start.StartPlugin,
	keepalive.KeepalivePlugin,
	respawn.RespawnPlugin,
	move.MovementPlugin,
	#world.WorldPlugin,
	#clientinfo.ClientInfoPlugin,
]
