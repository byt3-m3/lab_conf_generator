from marshmallow import Schema, fields

from gcg.schemas.snmp import BaseSNMPv2, BaseSNMPv3
from gcg.schemas.validators import IPValidator
from marshmallow.validate import OneOf


class IPv6Addr(Schema):
    ipv6_address = fields.Str()
    eui_64 = fields.Str()
    link_local = fields.Str()
    anycast = fields.Str()


class IPv4Addr(Schema):
    address = fields.Str(required=True, validate=IPValidator())
    netmask = fields.Str(required=True, validate=IPValidator())


class BaseInterface(Schema):
    link_id = fields.Str(required=True)
    dot1q = fields.Str()
    is_mgmt = fields.Boolean()
    description = fields.Str()
    bandwidth = fields.Str()
    ipv4_addrs = fields.List(fields.Nested(IPv4Addr))
    ipv6_addrs = fields.List(fields.Nested(IPv6Addr))


class BaseNode(Schema):
    hostname = fields.Str(required=True)
    domain = fields.Str(required=True)
    snmpv2 = fields.List(fields.Nested(BaseSNMPv2))
    snmpv3 = fields.List(fields.Nested(BaseSNMPv3))
    interfaces = fields.List(fields.Nested(BaseInterface))
