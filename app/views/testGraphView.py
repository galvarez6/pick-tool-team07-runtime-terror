from .ui.uiobjects import Ui_ListGraphConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog 
from PyQt5 import QtWidgets

from QGraphViz.QGraphViz import QGraphViz
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot


class ListGraphView(QDialog):
    def __init__(self, parent):
        super(ListGraphView, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ListGraphConfig()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setRowCount(50)
        self.setupGraph()
        self.addCheckBoxes()
        self.exec_()

    def setupGraph(self): 
        graph = self.ui.graph
        qgv = QGraphViz(
        # show_subgraphs=show_subgraphs,
        # node_selected_callback=node_selected,
        # edge_selected_callback=edge_selected,
        # node_invoked_callback=node_invoked,
        # edge_invoked_callback=edge_invoked,
        )

        qgv.new(Dot(Graph("Main_Graph")))

        n1 = qgv.addNode(qgv.engine.graph, "Node1", label="N1")
        n2 = qgv.addNode(qgv.engine.graph, "Node2", label="N2")
        n3 = qgv.addNode(qgv.engine.graph, "Node3", label="N3")
        n4 = qgv.addNode(qgv.engine.graph, "Node4", label="N4")
        n5 = qgv.addNode(qgv.engine.graph, "Node5", label="N5")
        n6 = qgv.addNode(qgv.engine.graph, "Node6", label="N6")

        qgv.addEdge(n1, n2, {})
        qgv.addEdge(n3, n2, {})
        qgv.addEdge(n2, n4, {"width":2})
        qgv.addEdge(n4, n5, {"width":4})
        qgv.addEdge(n4, n6, {"width":5,"color":"red"})
        qgv.addEdge(n3, n6, {"width":2})

        # Build the graph (the layout engine organizes where the nodes and connections are)
        qgv.build()

        qgv.save("test.gv")
        graph.layout().addWidget(qgv)

    def addCheckBoxes(self):
        num = 0
        while (num < self.ui.tableWidget.columnCount()):
            check_box = QtWidgets.QCheckBox()
            self.ui.tableWidget.setCellWidget(0, num, check_box)
            num += 1
        num = 0
        while (num <= self.ui.tableWidget.rowCount()):
            check_box = QtWidgets.QCheckBox()
            self.ui.tableWidget.setCellWidget(num + 1, 0, check_box)
            num += 1

