import struct
from collections import namedtuple

DNS_UNPK = namedtuple('DNS', 'pkt_id qr opcode aa tc rd ra rcode qdcount ancount nscount arcount')

def unpack_dns(pkt):
    tmp = struct.unpack("!HBBHHHH", pkt)
    qr = ((tmp[1] >> 7) & 1)
    opcode = ((tmp[1] >> 3) & 0x7)
    aa = ((tmp[1] >> 2) & 1)
    tc = ((tmp[1] >> 1) & 1)
    rd = (tmp[1] & 1)
    ra = ((tmp[2] >> 7) & 1)
    rcode = (tmp[2] & 0x7)

    return DNS_UNPK(pkt_id=tmp[0], qr=qr, opcode=opcode, aa=aa, tc=tc, rd=rd, ra=ra, rcode=rcode, qdcount=tmp[3], ancount=tmp[4], nscount=tmp[5], arcount=tmp[6])



def pack_dns(pkt_id, qr, opcode, aa, tc, rd, ra, rcode, qdcount, ancount, nscount, arcount):
    flags1 = (qr << 7) | (opcode << 3) | (aa << 2) | (tc << 1) | rd
    flags2 = (ra << 7) | rcode
    return struct.pack("!HBBHHHH", pkt_id, flags1, flags2, qdcount, ancount, nscount, arcount)

#test = pack_dns(1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
#print(unpack_dns(test))
