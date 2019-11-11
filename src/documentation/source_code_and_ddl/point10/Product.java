/*

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity(name = "Products")
@Setter
@Getter
@NoArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int productId;

    private String ProductName;
    private int UnitsOnStock;

    @ManyToMany(mappedBy = "products")
    Set<Supplier> suppliers = new HashSet<>();

    @ManyToMany(
            mappedBy = "includesProducts",
            fetch = FetchType.EAGER,
            cascade = CascadeType.PERSIST)
    Set<Invoice> canBeSoldIn = new HashSet<>();

    public Product(String productName, int unitsOnStock) {
        ProductName = productName;
        UnitsOnStock = unitsOnStock;
    }
}


 */