from tokenizer import Tokenizer
from binop import BinOp
from noop import NoOp
from unop import UnOp
from intval import IntVal
from assignernode import AssignerNode
from identifiernode import IdentifierNode
from printnode import PrintNode
from commandsnode import CommandsNode
from condnode import CondNode
from loopnode import LoopNode
from scannode import ScanNode
from vardecnode import VarDecNode


child = IntVal()
if isinstance(child, NoOp):
	print(True)