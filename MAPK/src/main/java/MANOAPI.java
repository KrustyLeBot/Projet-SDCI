Mano

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Random;
import java.io.IOException;
import java.net.*;
import java.io.*;
import java.util.regex.*;

/**
 * @author couedrao on 27/11/2019.
 * @project gctrl
 */
class MANOAPI {

    String deploy_gw(Map<String, String> vnfinfos) {
        String ip = "192.168.0." + (new Random().nextInt(253) + 1);
        Main.logger(this.getClass().getSimpleName(), "Deploying VNF ...");

        //printing
        for (Entry<String, String> e : vnfinfos.entrySet()) {
            Main.logger(this.getClass().getSimpleName(), "\t" + e.getKey() + " : " + e.getValue());
        }
        //TODO
        /*
        URL url;
        try {
            url = new URL("http://127.0.0.1:5001/restapi/compute/cvim1/new_vnf");
            HttpURLConnection httpCon = (HttpURLConnection) url.openConnection();
            httpCon.setRequestMethod("PUT");
            httpCon.setDoOutput(true);
            httpCon.setRequestProperty("Content-Type", "application/json");

            String payload = "{\"image\":\"krustylebot/repo:sdci_gw_virtualisee\"}";

            OutputStreamWriter osw = new OutputStreamWriter(httpCon.getOutputStream());
            osw.write(payload);
            osw.flush();
            osw.close();
            
            BufferedReader in = new BufferedReader(new InputStreamReader(httpCon.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                Pattern pattern = Pattern.compile("\"ip\": \"10.0.0.[0-9]\"");
                Matcher matcher = pattern.matcher(line);
                
                if(matcher.find()){
                    String[] split_list = line.split("\"",0);
                    ip = split_list[split_list.length-1];
                }
            }
            in.close();
            
        } catch (MalformedURLException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }
        */
        return ip;
    }

    List<String> deploy_multi_gws_and_lb(List<Map<String, String>> vnfsinfos) {
        List<String> ips = new ArrayList<>();
        //TODO

        for (Map<String, String> vnfsinfo : vnfsinfos) {
            ips.add(deploy_gw(vnfsinfo));
        }

        return ips;
    }
}
