import org.hibernate.Session;
import org.hibernate.Transaction;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

public class DatabasePerformer {

    public static void addNewProductPoint3(Session session) {
        Product product = Creator.createProduct();

        Transaction transaction = session.beginTransaction();
        session.save(product);
        transaction.commit();
    }

    public static void addNewSupplierPoint3(Session session) {
        Supplier supplier = Creator.createSupplier();

        Transaction transaction = session.beginTransaction();
        session.save(supplier);

        Product product = session.load(Product.class, 1);
//        product.setSupplier(supplier);
        transaction.commit();
    }

    public static void addNewSupplierAndProducts(Session session) {
        Supplier supplier = Creator.createSupplier();
        Product product = Creator.createProduct();
        Product product1 = Creator.createProduct();

        session.clear();
        Transaction transaction = session.beginTransaction();

        session.save(supplier);
        session.save(product);
        session.save(product1);

        supplier.products.add(product);
        supplier.products.add(product1);

        transaction.commit();
    }

    public static void addProductSupplierAndCategory(Session session) {
        Supplier supplier = Creator.createSupplier();
        Product product = Creator.createProduct();
        Category category = Creator.createCategory();

        session.clear();
        Transaction transaction = session.beginTransaction();

        session.save(supplier);
        session.save(product);
        session.save(category);

        supplier.products.add(product);
        category.products.add(product);
        transaction.commit();
    }

    public static void addInvoiceAndSell(Session session) {
        Supplier supplier = Creator.createSupplier();
        Product product = Creator.createProduct();
        Invoice invoice = Creator.createInvoice();

        session.clear();
        Transaction transaction = session.beginTransaction();

        session.save(supplier);
        session.save(product);
        session.save(invoice);

        supplier.products.add(product);
        product.canBeSoldIn.add(invoice);
        invoice.includesProducts.add(product);

        transaction.commit();
    }

    public static void addProductSupplierAndCategory(EntityManager entityManager) {
        Supplier supplier = Creator.createSupplier();
        Product product = Creator.createProduct();
        Category category = Creator.createCategory();

        entityManager.clear();

        EntityTransaction transaction = entityManager.getTransaction();
        transaction.begin();

        entityManager.persist(supplier);
        entityManager.persist(product);
        entityManager.persist(category);

        supplier.products.add(product);
        category.products.add(product);

        transaction.commit();
    }

    public static void addSupplierAndProduct(Session session) {
        Supplier supplier = Creator.createSupplier();
        Product product = Creator.createProduct();

        session.clear();
        Transaction transaction = session.beginTransaction();

        session.save(supplier);
        session.save(product);

        supplier.products.add(product);

        transaction.commit();
    }
}
