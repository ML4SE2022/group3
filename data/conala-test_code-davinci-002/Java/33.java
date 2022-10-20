import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ReadExcelFile {

	public static void main(String[] args) throws IOException {
		FileInputStream file = new FileInputStream(new File("C:\\Users\\Saurabh Dhingra\\workspace\\ReadExcelFile\\src\\readExcelFile\\ReadExcelFile.xlsx"));

		//Create Workbook instance holding reference to .xlsx file
		XSSFWorkbook workbook = new XSSFWorkbook(file);

		//Get first/desired sheet from the workbook
		XSSFSheet sheet = workbook.getSheetAt(0);

		//Iterate through each rows one by one
		Iterator<Row> rowIterator = sheet.iterator();

		FileOutputStream fos = new FileOutputStream("C:\\Users\\Saurabh Dhingra\\workspace\\ReadExcelFile\\src\\readExcelFile\\ReadExcelFile.txt");

		while(rowIterator.hasNext()){
			Row row = rowIterator.next();

			//For each row, iterate through all the columns
			Iterator<Cell> cellIterator = row.cellIterator();

			while(cellIterator.hasNext()){
				Cell cell = cellIterator.next();

				//Check the cell type and format accordingly
				switch(cell.getCellType()){
					case Cell.CELL_TYPE_