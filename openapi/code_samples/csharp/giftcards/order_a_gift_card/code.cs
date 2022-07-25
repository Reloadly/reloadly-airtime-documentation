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
          productId = "120",
          countryCode = "US",
          quantity = "1",
          unitPrice = "1",
          customIdentifier = "obucks10",
          senderName = "John Doe",
          recipientEmail = "anyone@email.com",
          recipientPhoneDetails = new {
            countryCode = "NG",
            phoneNumber = "8031934751"
          }
      });

      var message = new HttpRequestMessage(HttpMethod.Post, "https://giftcards/reloadly.com/orders") {
        Content = new StringContent(json, Encoding.UTF8, "application/json")
      };

      message.Headers.TryAddWithoutValidation("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
      message.Headers.TryAddWithoutValidation("Accept", "application/com.reloadly.giftcards-v1+json");

      using
      var httpClient = new HttpClient();
      var response = await httpClient.SendAsync(message);
      var responseBody = await response.Content.ReadAsStringAsync();
      var result = JsonConvert.DeserializeObject < dynamic > (responseBody);

      Console.WriteLine(result);
    }

  }
}