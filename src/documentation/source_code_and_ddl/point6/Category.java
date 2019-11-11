/*

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Setter
@Getter
public class Category {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int CategoryID;
    private String Name;

    @OneToMany
    @JoinColumn(name = "categoryId")
    List<Product> products = new ArrayList<>();

    public Category(String name) {
        this.Name = name;
    }
}

 */