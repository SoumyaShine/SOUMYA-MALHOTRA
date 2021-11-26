import streamlit as st
from  dbnew import Medicine,Customer,Bill
from sqlalchemy import inspect

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine
from sqlalchemy.sql.functions import mode


def open_db():
    '''function connects to database'''
    engine = create_engine('sqlite:///db.sqlite3')
    Session = sessionmaker(bind=engine)
    return Session()


st.title("Medical Inventory Application")
choices = ['Medicine','Customer','Bill','Show Details','Update Details','Delete Details']
selected_choice = st.selectbox("select an option",options=choices)

 

if selected_choice == choices[0]:
    st.title("Medicine")

    
    choices = ["Add Medicine","Update Medicine","Delete Medicine","Show Medicine"]
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice == choices[0]:
        st.header("Add Medicine")

        with st.form('add_medicine'):
           

            col1,col2,col3=st.columns(3)
            with col1:
                name = st.text_input("Enter medicine name",help="you can enter any medicine name") 
            with col2:
                id = st.number_input("Enter ID : ",value=0)
            with col3:
                comp_name = st.text_input("Enter company name : ")
            
            col1,col2=st.columns(2)
            with col1:
                units = st.number_input("Enter cost price : ")
            with col2:
                sales = st.number_input("Enter sale price : ")

            col1,col2=st.columns(2)
            with col1:
                quantity = st.number_input("Enter quantity : ",value=0)
            with col2:
                min_quantity = st.number_input("Enter min quantity to maintain : ",value=0)

            #sup_id = st.number_input("Enter supplier ID : ",value=0)

            submit_btn = st.form_submit_button(label="Add the medicine")

        if id and submit_btn:
            try:
                db = open_db()
                entry = Medicine(med_name=name,id=id, sale= sales, unit= units, quantity= quantity, min_quantity= min_quantity,comp_name= comp_name ) 
                db.add(entry)
                db.commit()
                db.close()
                st.success("Medicine information successfully saved")

                st.markdown(f'''
                ##### Medicine id - {id}
                - ###### Medicine name - {name}
                - ###### Company Name - {comp_name}
                - ###### Cost Price - {units}
                - ###### Sale Price - {sales}
                - ###### Quantity - {quantity}
                - ###### Minimum Quantity - {min_quantity}

                ''')

            except Exception as e:
                st.error(f"Could not save the details. {e}")    

    elif selected_choice == choices[1]:
     
        st.subheader("Update Medicine details")
        id = st.number_input("Medicine ID",value=0)
        db = open_db()
        result = db.query(Medicine).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Medicine"):


                col1,col2=st.columns(2)
                with col1:
                    name = st.text_input("Enter medicine name",value=result.med_name) 
                with col2:
                    comp_name = st.text_input("Enter company name : ",value=result.comp_name)
                
                col1,col2=st.columns(2)
                with col1:
                    units = st.number_input("Enter cost price : ",value=result.unit)
                with col2:
                    sales = st.number_input("Enter sale price : ",value=result.sale)

                col1,col2=st.columns(2)
                with col1:
                    quantity = st.number_input("Enter quantity : ",value=result.quantity)
                with col2:
                    min_quantity = st.number_input("Enter min quantity to maintain : ",value=result.min_quantity)

                #sup_id = st.number_input("Enter supplier ID : ",value=result.sup_id)

                submit_btn = st.form_submit_button("Update")

                
                
            if id and submit_btn:
                try:
                    
                    result.med_name=name
                    result.comp_name=name
                    result.sale=sales
                    result.unit=units
                    result.quantity=quantity
                    result.min_quantity=min_quantity
                    #result.sup_id=sup_id
                    db.commit()
                    st.success("Medicine information updated successfully ")



                    st.markdown(f'''
                    ##### Medicine id - {id}
                    - ###### Medicine name - {name}
                    - ###### Company Name - {comp_name}
                    - ###### Cost Price - {units}
                    - ###### Sale Price - {sales}
                    - ###### Quantity - {quantity}
                    - ###### Minimum Quantity - {min_quantity}

                    ''')

                
                except Exception as e:
                    st.error(f"Could not update the details. {e}")    

        db.close()      


        

    elif selected_choice== choices[2]:

        st.subheader("Delete Medicine details")
        id = st.number_input("Medicine ID",value=1)
        b =st.button("delete Medicine")
        
        if b:
            db = open_db()
            result = db.query(Medicine).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("removed")
            db.close()

        

    elif selected_choice == choices[3]:
        st.header("Show Medicine")
        db = open_db()
        medicine_list= db.query(Medicine)
        db.close()
        for item in medicine_list:
            st.markdown(f'''
            ####   Medicine Id - {item.id}
            * ### Medicine Name - {item.med_name}
            * ###  Sale Price - {item.sale}
            * ### Cost Price-  {item.unit}
            * ### Company Name - {item.comp_name}
            * ### {item.cost}
            * ### Quantity - {item.quantity} 
            * ### Minimum Quantity - {item. min_quantity}
            * ### Total Medicines Purchased - {item.purchased_medicines}
                ''')
      



elif selected_choice == choices[1]:
    st.header("Customer")
    choices = [' Add Customer Details','Update Customers Details','Delete  Customers Details','Show Customer Details']
    selected_choice = st.selectbox("select an option",options=choices)

 

    if selected_choice == choices[0]:
        with st.form('Add Customer Details'):
        
            col1,col2,col3=st.columns(3)
            with col1:
                id = st.number_input("Enter ID : ",value=0)
            with col2:
                name = st.text_input("Enter Customer's name") 
            with col3:
                contact = st.number_input("Enter Customer's contact number",value=0)
            
            email = st.text_input("Enter Customer's email id")
            med_purchased = st.number_input("Enter number of medicines customer purchased",value=0)

            submit_btn = st.form_submit_button(label="Add Customer's Details")


        if id and submit_btn:
            try:
                db = open_db()
                entry = Customer( id=id,cust_name=name, contact_number=contact, emailAddress= email,  med_purchased= med_purchased ) 
                db.add(entry)
                db.commit()
                db.close()
                st.success("Customer information successfully saved")

                
                st.markdown(f'''
                ##### Customer id - {id}
                - ###### Customer's Name - {name}
                - ###### Customer's Contact Number - {contact}
                - ###### Customer's email id - {email}
                - ###### Medicine Purchased - {med_purchased}
            ''')

                db.close()
            except Exception as e:
                st.error(f"Could not save the details. {e}") 

    elif selected_choice== choices[1]:
    
        st.subheader("Update Customer details")
        id = st.number_input("Customer ID",value=1)
        db = open_db()
        result = db.query(Customer).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("Update Customer Details"):   

                col1,col2=st.columns(2)
                
                with col1:
                    name = st.text_input("Enter Customer's name",value=result.cust_name) 
                with col2:
                    contact = st.number_input("Enter Customer's contact number",value=result.contact_number)
                    
                email = st.text_input("Enter Customer's email id",value=result.emailAddress)
                med_purchased = st.number_input("Enter number of medicines customer purchased",value=result.med_purchased)

                submit_btn = st.form_submit_button(label="Update Customer's Details")

            if id and submit_btn:
                try:
                    result.id=id
                    result.cust_name=name
                    result.contact_number= contact
                    result.emailAddress=email
                    result.med_purchased=med_purchased
                    db.commit()
                    st.success("Customer information updated successfully ")

                    st.markdown(f'''
                    ##### Customer id - {id}
                    - ###### Customer's Name - {name}
                    - ###### Customer's Contact Number - {contact}
                    - ###### Customer's email id - {email}
                    - ###### Medicine Purchased - {med_purchased}
                    ''')


                except Exception as e:
                    st.error(f"Could not save the details. {e}")    
        db.close()
 
    elif selected_choice== choices[2]:
        
        st.subheader("Delete Customer details")
        id = st.number_input("Customer ID",value=1)
        b =st.button("delete Customer")
        
        if b:
            db = open_db()
            result = db.query(Customer).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("customer information removed")
            db.close()

    elif selected_choice == choices[3]:
        st.header("Show Customer Details")
        db = open_db()
        customer_list= db.query(Customer)
        for item in customer_list:
            st.markdown(f'''
            #### Customer ID -  {item.id}
            * ### Customer Name - {item.cust_name}
            * ### Customer Contact Number - {item.contact_number}
            * ###  Customer Email Id - {item.emailAddress}
            * ### Medicines Purchased - {item.med_purchased}
            * ###  Total Amount {item.total_cost}
            ''')
        db.close()

        

elif selected_choice == choices[2]:
    st.header("Generate Bill Invoice")
    choices=['Add Bill Details','Update Bill Details','Delete Bill Details','Show Bill Details']
    selected_choice = st.selectbox("select an option",options=choices)
       
    if selected_choice == choices[0]:
        with st.form('Add Bill Details'):
            
            col1,col2=st.columns(2)
            with col1:
                id = st.number_input("Enter Bill id",value=0)
            with col2:
                date = st.date_input("Enter Date")
            
            col1,col2=st.columns(2)
            with col1:
                totalAmount = st.number_input("Enter total amount")
            with col2:
                discount = st.number_input("Enter discount in %")
            
            radio = st.radio(label="paymentType",options={"cash","online"})
            paidAmount=st.number_input(label="Paid Amount")
            newPrice = totalAmount* (1-(discount / 100))
            remainingAmount = (totalAmount-paidAmount)
            submit_btn = st.form_submit_button(label="Add Bill Details")

        if id and submit_btn:
            try:
                db = open_db()
                entry = Bill(bill_id=id, bill_date=date, paymentType = radio ,totalAmount = totalAmount,  discount = discount,  newPrice = newPrice , remainingAmount=remainingAmount, paidAmount= paidAmount  ) 
                db.add(entry)
                db.commit()
                db.close()
                st.success("Bill details successfully saved")


                st.markdown(f'''
                ##### Bill id - {id}
                - ###### Bill Date - {date}
                - ###### Customer's Total Amount - {totalAmount}
                - ###### Discount - {discount}
                - ###### Payable Amount- {newPrice}
                - ###### Remaining Amount - {remainingAmount}
                - ###### Paid Amount - {paidAmount}
                ''')

            except Exception as e:
                st.error(f"Could not save the details. {e}")    
        

    elif selected_choice== choices[1]:
    
        st.subheader("Update Bill details")
        id = st.number_input("Bill ID",value=0)
        db = open_db()
        result = db.query(Bill).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Bill"):  

                
                date = st.date_input("Enter Date")
                
                col1,col2=st.columns(2)
                with col1:
                    totalAmount = st.number_input("Enter total amount",value=result.totalAmount)
                with col2:
                    discount = st.number_input("Enter discount",value=result.discount)
            
                radio = st.radio(label="paymentType",options={"cash","online"})
                paidAmount=st.number_input(label="Paid Amount")
                newPrice = totalAmount* (1-(discount / 100))
                remainingAmount = (totalAmount-paidAmount)
                
                submit_btn = st.form_submit_button(label="Update Bill Details")

            if id and submit_btn:
                try:
                    result.bill_id=id
                    result.bill_date=date
                    result.totalAmount= totalAmount
                    result.discount=discount
                    result.newPrice=newPrice
                    result.remainingAmount=remainingAmount
                    result.paidAmount=paidAmount
                    db.commit()
                    st.success("Bill information updated successfully ")

                    st.markdown(f'''
                        ##### Bill id - {id}
                        - ###### Bill Date - {date}
                        - ###### Customer's Total Amount - {totalAmount}
                        - ###### Discount - {discount}
                        - ###### Payable Amount- {newPrice}
                        - ###### Remaining Amount - {remainingAmount}
                        - ###### Paid Amount - {paidAmount}
                        ''')

                except Exception as e:
                    st.error(f"Could not save the details. {e}")    
        db.close()      


    elif selected_choice== choices[2]:
        
        st.subheader("Delete Bill details")
        id = st.number_input("Bill ID",value=0)
        b =st.button("delete Bill")
        
        if b:
            db = open_db()
            result = db.query(Bill).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("bill information removed")
            db.close()

    elif selected_choice == choices[3]:
        st.header("Show Bill Details")
        db = open_db()
        bill_list= db.query(Bill)
        db.close()
        for item in bill_list:
            st.markdown(f'''
            #### Bill Id - {item.bill_id}
            * ### Bill Date - {item.bill_date}
            * ### Payment Type - {item.paymentType}
            * ### Total Amount - {item.totalAmount}
            * ### Discount - {item.discount}
            * ### New Amount after Discount - {item.newPrice}
            - ### Paid Amount - {item.paidAmount}
                ''')


elif selected_choice == choices[3]:
    st.title("Show Details")
        
    choices = ['Show Medicine',' Show Customer','Show Bill']
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice == choices[0]:
        st.header("Show Medicine")
        db = open_db()
        medicine_list= db.query(Medicine)
        db.close()
        for item in medicine_list:
            st.markdown(f'''
            ####   Medicine Id - {item.id}
            * ### Medicine Name - {item.med_name}
            * ###  Sale Price - {item.sale}
            * ### Cost Price-  {item.unit}
            * ### Company Name - {item.comp_name}
            * ###  Cost - {item.cost}
            * ### Quantity - {item.quantity} 
            * ### Minimum Quantity - {item. min_quantity}
            * ### Total Medicines Purchased - {item.purchased_medicines}
                ''')

    if selected_choice == choices[1]:
        st.header("Show Customer")
        db = open_db()
        customer_list= db.query(Customer)
        db.close()
        for item in customer_list:
            st.markdown(f'''
            #### Customer ID -  {item.id}
            * ### Customer Name - {item.cust_name}
            * ### Customer Contact Number - {item.contact_number}
            * ###  Customer Email Id - {item.emailAddress}
            * ### Medicines Purchased - {item.med_purchased}
            * ###  Total Amount {item.total_cost}
                ''')
            
    if selected_choice == choices[2]:
        st.header("Show Bill")
        db = open_db()
        bill_list= db.query(Bill)
        db.close()
        for item in bill_list:
            st.markdown(f'''
            #### Bill Id - {item.bill_id}
            * ### Bill Date - {item.bill_date}
            * ### Payment Type - {item.paymentType}
            * ### Total Amount - {item.totalAmount}
            * ### Discount - {item.discount}
            * ### New Amount after Discount - {item.newPrice}
            * ### Paid Amount - {item.paidAmount}
                ''')
            
elif selected_choice == choices[4]:
    st.subheader(" Update Details")

    choices = ['Update medicine details','Update Customer details','Update Bill Invoice details']
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice== choices[0]:
    
        st.subheader("Update Medicine details")
        id = st.number_input("Medicine ID",value=1)
        db = open_db()
        result = db.query(Medicine).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Medicine"):


                col1,col2,col3=st.columns(3)
                with col1:
                    name = st.text_input("Enter medicine name",help="you can enter any medicine name") 
                with col2:
                    id = st.number_input("Enter ID : ")
                with col3:
                    comp_name = st.text_input("Enter company name : ")
                
                col1,col2=st.columns(2)
                with col1:
                    units = st.number_input("Enter cost price : ")
                with col2:
                    sales = st.number_input("Enter sale price : ")

                col1,col2=st.columns(2)
                with col1:
                    quantity = st.number_input("Enter quantity : ")
                with col2:
                    min_quantity = st.number_input("Enter min quantity to maintain : ")

                submit_btn = st.form_submit_button(label="Update  medicine details")

                
                
            if id and submit_btn:
                try:
                    result.id=id
                    result.name=name
                    result.comp_name=name
                    result.sales=sales
                    result.units=units
                    result.quantity=quantity
                    result.min_quantity=min_quantity
                    db.commit()
                    st.success("Medicine information updated successfully ")



                    st.markdown(f'''
                    ##### Medicine id - {id}
                    - ###### Medicine name - {name}
                    - ###### Company Name - {comp_name}
                    - ###### Cost Price - {units}
                    - ###### Sale Price - {sales}
                    - ###### Quantity - {quantity}
                    - ###### Minimum Quantity - {min_quantity}
                    ''')

                
                except Exception as e:
                    st.error(f"Could not update the details. {e}")    

        db.close()      


    if selected_choice== choices[1]:
    
        st.subheader("Update Customer details")
        id = st.number_input("Customer ID",value=1)
        db = open_db()
        result = db.query(Customer).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Customer"):   

                col1,col2,col3=st.columns(3)
                with col1:
                        id = st.number_input("Enter ID : ")
                with col2:
                        name = st.text_input("Enter Customer's name") 
                with col3:
                        contact = st.number_input("Enter Customer's contact number")
                    
                email = st.text_input("Enter Customer's email id")
                med_purchased = st.number_input("Enter number of medicines customer purchased")

                submit_btn = st.form_submit_button(label="Add Customer's Details")

            if id and submit_btn:
                try:
                    result.id=id
                    result.name=name
                    result.contact= contact
                    result.email=email
                    result.med_pyrchased=med_purchased
                    db.commit()
                    st.success("Customer information updated successfully ")

                    st.markdown(f'''
                    ##### Customer id - {id}
                    - ###### Customer's Name - {name}
                    - ###### Customer's Contact Number - {contact}
                    - ###### Customer's email id - {email}
                    - ###### Medicine Purchased - {med_purchased}
                ''')


                except Exception as e:
                    st.error(f"Could not save the details. {e}")    
        db.close()


    if selected_choice== choices[2]:
    
        st.subheader("Update Bill details")
        id = st.number_input("Bill ID",value=1)
        db = open_db()
        result = db.query(Bill).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Bill"):  

                col1,col2=st.columns(2)
                with col1:
                    id = st.number_input("Enter Bill id")
                with col2:
                        date = st.date_input("Enter Date")
                
                col1,col2=st.columns(2)
                with col1:
                    totalAmount = st.number_input("Enter total amount")
                with col2:
                    discount = st.number_input("Enter discount")
            
                radio = st.radio(label="paymentType",options={"cash","online"})
                paidAmount=st.number_input(label="Paid Amount")
                newPrice = totalAmount* (1-(discount / 100))
                remainingAmount = (totalAmount-paidAmount)
                
                submit_btn = st.form_submit_button(label="Update Bill Details")

            if id and submit_btn:
                try:
                    result.id=id
                    result.date=date
                    result.totalAmount= totalAmount
                    result.discount=discount
                    result.newPrice=newPrice
                    result.remainingAmount=remainingAmount
                    result.paidAmount=paidAmount
                    db.commit()
                    st.success("Bill information updated successfully ")

                    st.markdown(f'''
                        ##### Bill id - {id}
                        - ###### Bill Date - {date}
                        - ###### Customer's Total Amount - {totalAmount}
                        - ###### Discount - {discount}
                        - ###### Payable Amount- {newPrice}
                        - ###### Remaining Amount - {remainingAmount}
                        - ###### Paid Amount - {paidAmount}
                    ''')

                except Exception as e:
                    st.error(f"Could not save the details. {e}")    
        db.close()      





elif selected_choice== choices[5]:
    st.subheader("delete detalis")

    choices = ['Delete Medicine details','Delete Customer details','Delete  Bill Invoice details']
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice== choices[0]:
        
        st.subheader("Delete Medicine details")
        id = st.number_input("Medicine ID",value=1)
        b =st.button("delete Medicine")
        
        if b:
            db = open_db()
            result = db.query(Medicine).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("medicine  information removed")
            db.close()

    elif selected_choice== choices[1]:
        
        st.subheader("Delete Customer details")
        id = st.number_input("Customer ID",value=1)
        b =st.button("delete Customer")
        
        if b:
            db = open_db()
            result = db.query(Customer).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("customer information removed")
            db.close()

    elif selected_choice== choices[2]:
        
        st.subheader("Delete Bill details")
        id = st.text_input("Bill ID",value=0)
        b =st.button("delete Bill")
        
        if b:
            db = open_db()
            result = db.query(Bill).get(id)
            if result:
                db.delete(result)
            
                db.commit()
                st.success("bill information removed")
            db.close()


       