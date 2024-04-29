import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class robotics {

    public static void main(String[] args) {
        try {
            String apiKey1 = "vR5470ZRclq0DkUkxYzofXN2ScqLc8";
            String apiKey2 = "wx7bzlcBxD2Dd4wWqkrJfDnfKUsIoC6AMp";

            URL url = new URL("https://www.thebluealliance.com/api/v3/team/frc2052");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("X-TBA-Auth-Key", apiKey1+apiKey2);

            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String line;
            StringBuilder response = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            System.out.println("Response:");
            System.out.println(response.toString());

            connection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}