# automatically generated by the FlatBuffers compiler, do not modify

# namespace: graph

import flatbuffers

class UIAddName(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUIAddName(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UIAddName()
        x.Init(buf, n + offset)
        return x

    # UIAddName
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UIAddName
    def NameIdx(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UIAddName
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def UIAddNameStart(builder): builder.StartObject(2)
def UIAddNameAddNameIdx(builder, nameIdx): builder.PrependInt32Slot(0, nameIdx, 0)
def UIAddNameAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def UIAddNameEnd(builder): return builder.EndObject()
