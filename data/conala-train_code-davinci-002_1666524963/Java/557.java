import java.util.ArrayList;
import java.util.List;

import org.apache.commons.math3.linear.RealMatrix;

public class MatrixToList {
    public static List<Double> matrixToList(RealMatrix matrix) {
        List<Double> list = new ArrayList<Double>();
        for (int i = 0; i < matrix.getRowDimension(); i++) {
            for (int j = 0; j < matrix.getColumnDimension(); j++) {
                list.add(matrix.getEntry(i, j));
            }
        }
        return list;
    }
}