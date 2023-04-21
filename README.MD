setting change to authenticated

i changed customer group permission so a cust can update flight (otherwise he cant book a seat)

i should handle situation where authorization key is not provided

handle where i delete things that doesnt exist

why when im creating a user that is related to a customer model it doesnt automatically understands thats a customer???

*******validators
**********react
******permissions
***********Craete a ready to use data
******tests

to book a flight: LoginRequiredMixin

Views will be separated like this:
Auth view:
    -Register
    -Refresh 
    -Login
    -Logout


Admin view:
    -Admins list
    -Admin detail


Users view:
    -Users list
    -User detail


Users roles view:
    -User roles list
    -User role detail


Country view:
    -Countries list
    -country detail


Customer view:
    -Customers list
    -Customer detail


Airline view:
    -Airlines list
    -Airline detail


Flight view:
    -Flights list
    -Flight detail

#UNKNOWN
    -Tickets list
    -Ticket detail