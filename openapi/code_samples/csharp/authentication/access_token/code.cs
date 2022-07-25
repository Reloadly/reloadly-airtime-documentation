using System;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;

namespace WebAPIClient {
  class Program {

    static async Task Main(string[] args) {
      await ApiCall();
    }

    private static async Task ApiCall() {
      var json = JsonConvert.SerializeObject(new {
        client_id = "qwcLzXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", 
        client_secret = "7kscVxQZ32-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", 
        grant_type = "client_credentials", 
        audience = "INSERT_PRODUCT_SERVER_URL_HERE"
      });

      var message = new HttpRequestMessage(HttpMethod.Post, "https://auth.reloadly.com/oauth/token");
      
      message.Headers.TryAddWithoutValidation("Content-Type", "application/json");

      using
      var httpClient = new HttpClient();
      var response = await httpClient.SendAsync(message);
      var responseBody = await response.Content.ReadAsStringAsync();
      var result = JsonConvert.DeserializeObject < dynamic > (responseBody);

      Console.WriteLine(result);
    }

  }
}