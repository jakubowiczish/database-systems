import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Embeddable;

@Getter
@Setter
@Embeddable
@NoArgsConstructor
public class Address {

    private String Street;
    private String City;
    private String Country;

    public Address(String street, String city, String country) {
        Street = street;
        City = city;
        Country = country;
    }
}
