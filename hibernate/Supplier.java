import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "Suppliers")
@Getter
@Setter
@NoArgsConstructor
public class Supplier {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int supplierId;

    @ManyToMany
    @JoinTable(
            name = "ProductSupplier",
            joinColumns = {@JoinColumn(name = "supplierId")},
            inverseJoinColumns = {@JoinColumn(name = "productId")}
    )
    Set<Product> products = new HashSet<>();

    @Embedded
    Address address;

    public Supplier(String companyName, String street, String city) {
        this.address = new Address(companyName, street, city);
    }
}
