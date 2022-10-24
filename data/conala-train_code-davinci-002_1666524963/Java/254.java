import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class XlsxWriter {

	public static void main(String[] args) throws IOException {
		String[] columns = { "Name", "Email", "Date Of Birth", "Salary" };
		String path = "C:\\Users\\user\\Desktop\\";
		String fileName = "Employee.xlsx";
		String sheetName = "Employee";
		List<Employee> list = new ArrayList<>();
		list.add(new Employee("Rajeev Singh", "rajeev@example.com", "1991-04-21", 9000000.0));
		list.add(new Employee("Thomas cook", "thomas@example.com", "1980-07-02", 6500000.0));
		list.add(new Employee("Steve Maiden", "steve@example.com", "1978-09-23", 7500000.0));
		list.add(new Employee("Brad pit", "brad@example.com", "1956-12-02", 8500000.0));
		list.add(new Employee("Herry Porter", "herry@example.com", "1961-01-25", 7500000.0));
		list.add(new Employee("Clark Man", "clark@example.com", "1951-11-12", 6500000.0));
		list.add(new Employee("Paul Robinson", "paul@example.com", "1964-01-31", 5500000.0));
		list.add(new Employee("Buffet", "buffet@example.com",