from telethon import TelegramClient
import os

api_id = os.environ["TG_API_ID"]
api_hash = os.environ["TG_API_HASH"]

client = TelegramClient("tg", api_id, api_hash)


async def TuringLab():
    longterm_sharecodes = {
        "farm": (
            "162e1936b67c44e489d5e9f2c19bf19e",
            "72d794ac40b5407b89b06dbf49b935b1",
        ),
        "pet": ("MTE1NDAxNzgwMDAwMDAwNDMwMzM5NjE=", "MTE1NDQ5MzYwMDAwMDAwNDMwMzM5Njk="),
        "bean": (
            "4npkonnsy7xi3dna3iw4in6t2ixkufx5rmoo5uq",
            "e7lhibzb3zek3gtlvnownonyawhg3fnp5txiq2a",
        ),
        "jxfactory": ("Ll_BJZ0ycq8aIipapE1cUw==", "LfF5eSL8m4K8hD1b8MztSw=="),
        "ddfactory": (
            "T0225KkcRxgY8QbQJxn3lv4CdwCjVWnYaS5kRrbA",
            "T0225KkcRBkao1zedRr2x_8PdwCjVWnYaS5kRrbA",
        ),
    }

    shortterm_sharecodes = {
        "sgmh": (
            "T0225KkcRxgY8QbQJxn3lv4CdwCjVQmoaT5kRrbA",
            "T0225KkcRBkao1zedRr2x_8PdwCjVQmoaT5kRrbA",
        ),
        "jxcfd": (
            "77A1D53B422AFAB2B3413E83EFBBF6A8B7D50E6705F2837BCB5FE159947080EE",
            "5249F471E83BFD0101028553F06559B0B7BEC7F80A41145E3D6D7DE1D0B28E33",
        ),
        "jdglobal": (
            "dGdLdDVGY1BxNEdFenBscFRENGJjRU10V0NCZTY2ak0ralZpdkRPQWdUOD0=",
            "Nndjek9NbFpPQzhtYnBTU011V3dzTDVDSFBIUlBybVBqdjJjUElPdUp1dz0=",
        ),
    }

    sharecodes = {**longterm_sharecodes, **shortterm_sharecodes}

    for s in sharecodes:
        msg = "&".join(sharecodes[s])
        await client.send_message("@TuringLabbot", f"/submit_activity_codes {s} {msg}")


async def LvanLamCommitCode():
    longterm_sharecodes = {
        "jdzz": ("S5KkcRxgY8QbQJxn3lv4Cdw", "S5KkcRBkao1zedRr2x_8Pdw"),
        "jdcrazyjoy": (
            "AfTkMxFWZKDj6vs1Q8SPuqt9zd5YaBeE",
            "1ldyJmZ3vJwHoXm_caQTq6t9zd5YaBeE",
        ),
        "jdcash": ("eU9Ya-qzYq4h9m3WyXob1Q", "eU9YaOuxMPQvpG7XmHsW1Q"),
    }

    for s in longterm_sharecodes:
        msg = "&".join(longterm_sharecodes[s])
        await client.send_message("@LvanLamCommitCodeBot", f"/{s} {msg}")


with client:
    client.loop.run_until_complete(TuringLab())
    client.loop.run_until_complete(LvanLamCommitCode())
