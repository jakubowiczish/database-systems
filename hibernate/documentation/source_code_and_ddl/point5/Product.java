/*

import lombok.*;

import javax.persistence.*;
import java.util.Set;

@Entity(name = "Products")
@Getter
@Setter
@NoArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int productId;

    private String ProductName;
    private int UnitsOnStock;

    @ManyToMany(mappedBy = "products")
    Set<Supplier> suppliers;

    public Product(String productName, int unitsOnStock) {
        ProductName = productName;
        UnitsOnStock = unitsOnStock;
    }
}

 */