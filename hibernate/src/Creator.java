import java.util.Scanner;

public class Creator {

    public static Product createProduct() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the product name:");
        String productName = scanner.nextLine();

        System.out.println("Enter state of warehouse:");
        int unitsInStock = scanner.nextInt();

        return new Product(productName, unitsInStock);
    }

    public static Supplier createSupplier() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter company name:");
        String companyName = scanner.nextLine();

        System.out.println("Enter street:");
        String street = scanner.nextLine();

        System.out.println("Enter city:");
        String city = scanner.nextLine();

        return new Supplier(companyName, street, city);

    }

    public static Category createCategory() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter category name:");
        String categoryName = scanner.nextLine();

        return new Category(categoryName);
    }

    public static Invoice createInvoice() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter invoice number:");
        int invoiceNumber = scanner.nextInt();

        System.out.println("Enter quantity:");
        int quantity = scanner.nextInt();

        return new Invoice(invoiceNumber, quantity);
    }
}
