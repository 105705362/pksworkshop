package hello;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpEntity;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class Application {

	private static final Logger log = LoggerFactory.getLogger(Application.class);

	public static void main(String args[]) {
		SpringApplication.run(Application.class);
	}

	@Bean
	public RestTemplate restTemplate(RestTemplateBuilder builder) {
		return builder.build();
	}

	@Value("${BACKEND_ENDPOINT:http://localhost:5000}")
	private String endpoint;

	@Bean
	public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
		log.info(endpoint);
		Person p = new Person();
		p.setName("pname");
		HttpEntity<Person> request = new HttpEntity<Person>(p);

		return args -> {
			Person person = restTemplate.postForObject(endpoint, request, Person.class);
			log.info(person.toString());
		};

		// return args -> {
		// Person person = restTemplate.getForObject(
		// endpoint, Person.class);
		// log.info(person.toString());
		// };
	}
}
