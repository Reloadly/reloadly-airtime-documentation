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
        phone = "03238482221", 
        countryCode = "PK" 
      });

      var message = new HttpRequestMessage(HttpMethod.Post, "https://topups.reloadly.com/mnp-lookup/operators");

      message.Headers.TryAddWithoutValidation("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
      message.Headers.TryAddWithoutValidation("Accept", "application/com.reloadly.topups-v1+json");
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