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
        URL url;
        try {
            Process process = Runtime.getRuntime().exec("vim-emu compute start -d dc1 -n gw2_virtualisee -i krustylebot/repo:sdci_containernet");
            StringBuilder output = new StringBuilder();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream()));

            String res;
            String line;
            while ((line = reader.readLine()) != null) {
                Pattern pattern = Pattern.compile("\"ip\": \"10.0.0.[0-9]\"");
                Matcher matcher = pattern.matcher(line);

                Main.logger(this.getClass().getSimpleName(), "LINE: " + line);
                
                if(matcher.find()){
                    String[] split_list = line.split("\"",0);
                    ip = split_list[split_list.length-1];
                }
            }
            Main.logger(this.getClass().getSimpleName(), "IP GW VIRTUALISEE: " + ip);
            
        } catch (MalformedURLException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }

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
