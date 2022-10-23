import hep.aida.*;
import java.util.Random;

public class Hist2DColorBar {
    public static void main(String[] args) {
        IAnalysisFactory af = IAnalysisFactory.create();
        ITree tree = af.createTreeFactory().create();
        IHistogramFactory hf = af.createHistogramFactory(tree);
        IPlotter plotter = af.createPlotterFactory().create("Plot");
        IHistogram2D h2d = hf.createHistogram2D("h2d", 50, -3, 3, 50, -3, 3);
        Random r = new Random();
        for (int i = 0; i < 10000; i++) {
            double x = r.nextGaussian();
            double y = r.nextGaussian();
            h2d.fill(x, y);
        }
        plotter.region(0).plot(h2d);
        plotter.show();
        plotter.interact();
    }
}