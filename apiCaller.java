
import java.io.BufferedReader;
import java.util.Scanner;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class apiCaller {

    
    private static final String USER_AGENT = "Mozilla/5.0";
    
    
    public static void main(String[] args) throws IOException {
        Scanner scanf = new Scanner(System.in);
        String GET_URL = "http://127.0.0.1:8000/getTotalStudentAttendance/";
        System.out.println("Enter prn:");
        String prn = scanf.nextLine();
        GET_URL = GET_URL+prn;
        sendHttpGETRequest(GET_URL);
    }

    private static void sendHttpGETRequest(String GET_URL) throws IOException {
        URL obj = new URL(GET_URL);
        HttpURLConnection httpURLConnection = (HttpURLConnection) obj.openConnection();
        httpURLConnection.setRequestMethod("GET");
        httpURLConnection.setRequestProperty("User-Agent", USER_AGENT);
        int responseCode = httpURLConnection.getResponseCode();
        // System.out.println("GET Response Code :: " + responseCode);
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in .readLine()) != null) {
                response.append(inputLine);
            } in .close();

            // print result
            System.out.println(response.toString());

            
        } else {
            System.out.println("GET request not worked");
        }

        // for (int i = 1; i <= 8; i++) {
        //     System.out.println(httpURLConnection.getHeaderFieldKey(i) + " = " + httpURLConnection.getHeaderField(i));
        // }

    }
}