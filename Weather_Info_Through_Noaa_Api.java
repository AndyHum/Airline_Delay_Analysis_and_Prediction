package weather;
// Can be used to extract weather data from NOAA Api, though our project didn`t use it due to insufficient time.
import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;


public class Weather_Info_Through_Noaa_Api {

    public static String requests(String httpUrl, String httpArg) {
        BufferedReader reader = null;
        String result = null;
        StringBuffer sbf = new StringBuffer();
        httpUrl = httpUrl+ "?" + httpArg;

        try {
            URL url = new URL(httpUrl);
            HttpURLConnection connection = (HttpURLConnection) url
                    .openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Token","rrdnbnBlwqrVmuoIFcPcJNorbAftVXWW");
            connection.connect();
            InputStream is = connection.getInputStream();
            reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            String strRead = null;
            while ((strRead = reader.readLine()) != null) {
                sbf.append(strRead);
                sbf.append("\r\n");
            }
            reader.close();
            result = sbf.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
}
    public static void main(String []args ){
    	
    	String httpUrl="https://www.ncdc.noaa.gov/cdo-web/api/v2/data";
    	String httpArgs="datasetid=PRECIP_HLY&datatypeid=&locationid=ZIP:02115&startdate=2010-05-01&enddate=2010-05-01";
    	String out=requests(httpUrl, httpArgs);
    	
    	/*httpUrl="https://www.ncdc.noaa.gov/cdo-web/api/v2/locationcategories/ZIP";
    	httpArgs="02155";
    	https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?locationid=ZIP:02148
    	String out=requests(httpUrl, httpArgs);*/
    			
    	System.out.println(out);
    }
}