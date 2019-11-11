import org.hibernate.cfg.Configuration;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class MainJpa {

    private static EntityManagerFactory entityManagerFactory;

    static {
        try {
            Configuration configuration = new Configuration();
            configuration.configure();

            entityManagerFactory = configuration.buildSessionFactory();
        } catch (Throwable ex) {
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static void main(final String[] args) throws Exception {
        final EntityManager entityManager = getEntityManager();

        try {
            DatabasePerformer.addProductSupplierAndCategory(entityManager);
        } finally {
            entityManager.close();
        }
    }

    private static EntityManager getEntityManager() {
        if (entityManagerFactory == null) {
            entityManagerFactory = Persistence.createEntityManagerFactory("derby");
        }

        return entityManagerFactory.createEntityManager();
    }
}