/*

import lombok.*;

import javax.persistence.*;

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

    public Product(String productName, int unitsOnStock) {
        ProductName = productName;
        UnitsOnStock = unitsOnStock;
    }
}

*/