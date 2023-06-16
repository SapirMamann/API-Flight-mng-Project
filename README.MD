setting change to authenticated

<!-- user in models has null=true because it gives error (needs to be changed) -->

i changed customer group permission so a cust can update flight (otherwise he cant book a seat)

<!-- i should handle situation where authorization key is not provided -->
delete flight

if unlogged user wants to book flight he must login/ sign up
handle where i delete things that doesnt exist
 
formik to add airline company

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