# Online Paid Table Booking System in Chain Restaurants
A chain of restaurants provides an online paid table booking system for customers to make a reservation in advance for their dining. Customers can reserve tables by choosing the preferred date, time, number of people, restaurant location and paying a booking fee upfront. Customers can also modify or cancel their bookings through the system. Restaurant stuffs can confirm or cancel the reservations accordingly.

## Brief Use Case Description
| Use Case | Brief Use Case Description |
|----------|----------------------------|
| Customer Register | User enters new customer account data, and the system creates a customer account record. |
| Customer Login | User enters customer account number and password to login to the system. |
| Book a table | User enters the table booking page and reserve tables by choosing the preferred date, time, number of people, restaurant location and paying a booking fee upfront. |
| Cancel booking | User cancels the booking right after making a successful reservation or in the booking history. |
| Modify booking details | User modifies booking details like the preferred date, time, number of people and restaurant location from the booking history. |
| Restaurant stuff confirms a reservation | Restaurant stuff confirms a reservation after check the availablity of the table that the customer has required. |
| Restaurant stuff cancels a reservation | Restaurant stuff cancels a reservation and notifies the customer by text message under specific conditions(e.g., the restaurant is forced to be closed). |

## Full Developed Use Case Descriptions of Book a table use case
<table>
<style>
    th {
        text-align: left;
    }
</style>
  <tr>
    <th>Use case name:</th>
    <td>Book a table.</td>
  </tr>
  <tr>
    <th>Scenario:</th>
    <td>Book a table online.</td>
  </tr>
  <tr>
    <th>Triggering event:</th>
    <td>A registered customer wants to book a table online.</td>
  </tr>
  <tr>
    <th>Brief description:</th>
    <td>User enters the table booking page and reserve tables by choosing the preferred date, time, number of people, restaurant location and paying a booking fee upfront.</td>
  </tr>
  <tr>
    <th>Actors:</th>
    <td>Customer.</td>
  </tr>
  <tr>
    <th>Related use cases:</th>
    <td>Might be invoked by the Cancel Booking use case.</td>
  </tr>
  <tr>
    <th>Stakeholders:</th>
    <td>Restaurant stuff.</td>
  </tr>
  <tr>
    <th>Preconditions:</th>
    <td>Booking system must be available.</br>Online payment system must be available.</td>
  </tr>
  <tr>
    <th>Postconditions:</th>
    <td>The reservation must be created and saved.</br>Credit/debit card information used for online payment must be validated.</br>An upfront payment must be made.</td>
  </tr>
  <tr>
    <th>Flow of activities:</th>
    <td>
        <table border="0" style="border-collapse: collapse; width: 100%">
            <thead>
                <tr>
                    <th>Actor</th>
                    <th>System</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        1. Customer indicates desire to book a table and enters booking details.
                        </br></br>
                        2. Customer enters credit/debit card information.
                    </td>
                    <td>
                        1.1 System creates and saves the reservation.
                        </br>
                        1.2 System prompts for credit/debit card.
                        </br></br>
                        2.1 System verifies authorization for credit/debit card.
                        </br>
                        2.2 System processes the payment.
                        </br>
                        2.3 System prompts the payment is successful or unsuccessful.
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
  </tr>
  <tr>
    <th>Exception conditions:</th>
    <td>
        1.1 The booking details are not valid.
        </br>
        1.2 Credit/debit information isn't valid.
    </td>
  </tr>
</table>