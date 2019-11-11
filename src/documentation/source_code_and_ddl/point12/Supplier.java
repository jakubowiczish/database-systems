/*

import javax.persistence.Entity;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Supplier extends Company {

    public String bankAccountNumber;


    @OneToMany
    @JoinColumn(name = "SUPPLIED_BY")
    private Set<Product> supplies = new HashSet<>();

    public Supplier() {
        super();
    }

    public Supplier(String companyName, String street, String city, String account) {
        super(companyName, street, city);
        bankAccountNumber = account;
    }

    public void addSuppliedProduct(Product p) {
        supplies.add(p);
        p.setSuppliedBy(this);
    }

    public boolean suppliesProduct(Product p) {
        return supplies.contains(p);
    }
}


 */