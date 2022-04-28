from argparse import ArgumentParser
from typing import Any

from zerver.lib.management import ZulipBaseCommand


class Command(ZulipBaseCommand):
    help = """Change realm's invite_required setting."""

    def add_arguments(self, parser: ArgumentParser) -> None:
        self.add_realm_args(parser, required=True)
        parser.add_argument('--invite-required', dest='invite_required', action='store_true')
        parser.add_argument('--no-invite-required', dest='invite_required', action='store_false')
        parser.set_defaults(invite_required=True)

    def handle(self, *args: Any, **options: str) -> None:
        realm = self.get_realm(options)
        assert realm is not None  # Should be ensured by parser

        print(f"Setting invite required to {options['invite_required']}")

        realm_invite_required = options['invite_required']
        realm.invite_required = realm_invite_required
        realm.save()
        print('Done!')
