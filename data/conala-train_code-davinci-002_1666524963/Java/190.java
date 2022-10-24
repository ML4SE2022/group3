import java.util.ArrayList;
import java.util.List;

import org.apache.commons.math3.ml.clustering.CentroidCluster;
import org.apache.commons.math3.ml.clustering.KMeansPlusPlusClusterer;
import org.apache.commons.math3.ml.clustering.MultiKMeansPlusPlusClusterer;
import org.apache.commons.math3.ml.distance.EuclideanDistance;

public class KMeans {

    public static void main(String[] args) {
        List<Point> points = new ArrayList<Point>();
        points.add(new Point(1));
        points.add(new Point(2));
        points.add(new Point(3));
        points.add(new Point(4));
        points.add(new Point(5));
        points.add(new Point(6));
        points.add(new Point(7));
        points.add(new Point(8));
        points.add(new Point(9));
        points.add(new Point(10));

        KMeansPlusPlusClusterer<Point> clusterer = new KMeansPlusPlusClusterer<Point>(2, 1000, new EuclideanDistance());
        List<CentroidCluster<Point>> clusterResults = clusterer.cluster(points);
        for (CentroidCluster<Point> cluster : clusterResults) {
            System.out.println("Cluster center: " + cluster.getCenter().getPoint()[0]);
            System.out.println("Points: ");
            for (Point point : cluster.getPoints()) {
                System.out.println(point.getPoint()[0]);
            }
        }
    }
}

class Point {
    private double[] point;

    public Point(double x) {
        point = new double[] { x };
    }

    public double[] getPoint() {
        return point;
    }
}