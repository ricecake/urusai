# -*- coding: utf-8 -*-

import urusai_plugin
import re

class pluginHelp(urusai_plugin.MucMessage):
    triggers = {
        "^help$": "List",
        "^help\s": "Info"
    }

    @staticmethod
    def triggerList(fromName, fromJid, message):
        reply_fmt = "Available plugins: {0}\nTo get detailed information about module's possibility use \"help <MODULE>\"."
        [muc, author] = fromName.split("/", 1)
        plugins = urusai_plugin.getAvailablePlugins(muc)
        return reply_fmt.format(" ".join(plugins))

    @staticmethod
    def triggerInfo(fromName, fromJid, message):
        plugin = re.match(r"^help\s(.+)$", message).group(1)
        [muc, author] = fromName.split("/", 1)
        return urusai_plugin.getPluginDocs(muc, plugin)