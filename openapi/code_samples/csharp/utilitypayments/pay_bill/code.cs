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
         subscriberAccountNumber = "04223568280",
         amount = "1000",
         billerId = "5",
         useLocalAmount = false
      });

      var message = new HttpRequestMessage(HttpMethod.Post, "https://utilities.reloadly.com");

      message.Headers.TryAddWithoutValidation("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
      message.Headers.TryAddWithoutValidation("Accept", "application/com.reloadly.utilities-v1+json");
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