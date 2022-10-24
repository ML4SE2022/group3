import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.collections15.Transformer;

import edu.uci.ics.jung.algorithms.layout.CircleLayout;
import edu.uci.ics.jung.algorithms.layout.Layout;
import edu.uci.ics.jung.graph.DirectedSparseGraph;
import edu.uci.ics.jung.graph.Graph;
import edu.uci.ics.jung.visualization.BasicVisualizationServer;
import edu.uci.ics.jung.visualization.decorators.ToStringLabeller;
import edu.uci.ics.jung.visualization.renderers.Renderer.VertexLabel.Position;

public class GraphViewer {

	public static void main(String[] args) {
		Graph<Integer, String> g = new DirectedSparseGraph<Integer, String>();
		g.addVertex((Integer)1);
		g.addVertex((Integer)2);
		g.addVertex((Integer)3);
		g.addEdge("Edge-A", 1,2);
		g.addEdge("Edge-B", 2,3);

		// The Layout<V, E> is parameterized by the vertex and edge types
		Layout<Integer, String> layout = new CircleLayout<Integer, String>(g);
		layout.setSize(new Dimension(300,300)); // sets the initial size of the space
		// The BasicVisualizationServer<V,E> is parameterized by the edge types
		BasicVisualizationServer<Integer,String> vv = new BasicVisualizationServer<Integer,String>(layout);
		vv.setPreferredSize(new Dimension(350,350)); //Sets the viewing area size

		Transformer<Integer,Paint> vertexPaint = new Transformer<Integer,Paint>() {
			public Paint transform(Integer i)