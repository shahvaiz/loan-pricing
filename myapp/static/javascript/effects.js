// global variables
var user_county;
var state_county;
//var derived_loan_amount;
var guided_value;
var guided_loan_amount;
var	title_rates =  [
	[4.67, 3.97, 3.34, 2.65],
	[2.78, 2.21, 1.94, 1.68],
	[4.68, 4.44, 4.08, 2.7],
	[2.9, 2.7, 2.3, 1.85],
	[6.84, 6.12, 5.4, 4.5],
	[5.4, 4.68, 3.96, 2.8]
	];
	var a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]];
// show or hide input fields on the homepage based on whether user selects "purchase", "refinance", etc.
// rename placeholder values to guide user during input (i.e. rename Property Value to Purchase Price)
function yesNo() {
    var e = document.getElementById("id_loan_type");
    var x = document.getElementById("loan_balance_box");
    var w = document.getElementById("cash_out_box");
    var z = document.getElementById("down_payment_box");


    //var w = document.getElementById("id_cash_out");
    if (e.value == "refi_cash_out") {
        x.style.display = 'block';
        w.style.display = 'block';
        z.style.display = 'none';
        document.getElementById("label_property_value").innerHTML = "Property Value";
    }

    else if (e.value == "refi_rate_term") {
        x.style.display = 'block';
        w.style.display = 'none';
        z.style.display = 'none';
        document.getElementById("label_property_value").innerHTML = "Property Value";
    }

    else if (e.value == "purchase") {
        x.style.display = 'none';
        w.style.display = 'none';
        z.style.display = 'block';
        document.getElementById("label_property_value").innerHTML = "Purchase Price";

    }
}

function loan_amount_tooltip() {
  if ($('#id_loan_type').val() == 'refi_cash_out') {
    guided_value = parseInt($('#id_loan_balance').val()) + parseInt($('#id_cash_out').val());
	guided_loan_amount=guided_value;
    guided_value_formatted = parseFloat(guided_value);
    guided_value_formatted = (guided_value_formatted).formatMoney(0, '.', ',');
    $("#new").html(guided_value_formatted);
  }

    else if ($('#id_loan_type').val() == 'refi_rate_term') {
      guided_value = $('#id_loan_balance').val();
	  guided_loan_amount=guided_value;
      guided_value_formatted = parseFloat(guided_value);
      guided_value_formatted = (guided_value_formatted).formatMoney(0, '.', ',');
      $("#new").html(guided_value_formatted);

    }

  // purchase
    else {
      guided_value = parseInt($("#id_property_value").val()) - parseInt($("#id_down_payment").val());
	  guided_loan_amount=guided_value;
      guided_value_formatted = parseFloat(guided_value);
      guided_value_formatted = (guided_value_formatted).formatMoney(0, '.', ',');

      // prevent negative loan amounts
      if (guided_value >= 0) {
        $("#new").html(guided_value_formatted);
      }
      else
        $("#new").html(0);

    }
}

  //  "digits": 2,
  //  "radixPoint": "",

function maskInputValues() {

    $('#id_property_value').inputmask("currency", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 0,
    "integerDigits": 7,
    "allowMinus": false,
    "autoUnmask": true // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });

    $('#id_loan_balance').inputmask("currency", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 0,
    "integerDigits": 7,
    "allowMinus": false,
    "autoUnmask": true
     // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });

  $('#id_cash_out').inputmask("currency", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 0,
    "integerDigits": 7,
    "allowMinus": false,
    "autoUnmask": true // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });

  $('#id_down_payment').inputmask("currency", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 0,
    "integerDigits": 7,
    "allowMinus": false,
    "autoUnmask": true // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });

  $('#id_loan_amount_calculator').inputmask("currency", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 0,
    "integerDigits": 7,
    "allowMinus": false,
    "autoUnmask": true // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });

    // this the currency mask. it applies the formatting when the user enters a value
  $('#id_interest_rate').inputmask("decimal", {
    "rightAlign": false,
    "placeholder": "",
    "digits": 3,
    "integerDigits": 2,
    "allowMinus": false,
    "autoUnmask": true,
    "suffix": '%'
    //"radixFocus": false // this option will unmask value so that the raw, unformatted value is evaluated for validations, and sent to the View
  });
}
function validation_rules() {


  $('#mainForm').validate({ // initialize the plugin
                onkeyup: function (element) {
                    $(element).valid()

                },


                    rules: {

                        loan_amount: {
                            min: 50000,
                            max: 3000000,
                            number: true
                        },

                       /* property_value: {
                            min: 50000,
                            max: 10000000,
                            number: true
                        },*/

                        loan_balance: {
                            min: 50000,
                            max: 3000000,
                            number: true
                        },
                        zip_code: {
                            minlength: 5,
                            number: true
                        },
                        credit_score: {
                            min: 300,
                            max: 850,
                            number: true
                        }
                    },
                      messages: {
                        loan_amount: "Please enter a value between $50,000 and $3M",
                        property_value: "Please enter a value between $50,000 and $10M",
                        loan_balance: "Please enter a value between $50,000 and $3M",
                        interest_rate: "Please enter a value less than 20%",
                        }
        });

 $("#id_property_value").rules( "add", {
    min:40001
  });

}


function validation_rules_application() {


$("#loan_info_form").validate({

  // set these attributes to False to enforce validations upon clicking "submit," rather than onkeyup
  onfocusout: false,
  onkeyup: false,

    rules: {
      first_name: {
        required: true,
        lettersonly: true
      },

      last_name: {
        required: true,
        lettersonly: true
      },

      phone_number: {
        phoneUS: true
      },

      email: {
        required: true,
        email: true
      }
    }, // end of rules

    messages: {
      // first_name: "custom message"
    } // end of messages
  }); // end of validate method
}

// adding custom validations: http://jqueryvalidation.org/jQuery.validator.addMethod/
// https://github.com/jzaefferer/jquery-validation/tree/master/src/additional
function customValidations() {

  jQuery.validator.addMethod("test", function(value, element) {
      return this.optional(element) || /^.+@gmail.com$/.test(value);
  },"here is my test");

  $.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z]+$/i.test(value);
  }, "Letters only please");

  $.validator.addMethod("phoneUS", function(phone_number, element) {
    phone_number = phone_number.replace(/\s+/g, "");
    return this.optional(element) || phone_number.length > 9 &&
    phone_number.match(/^(\+?1-?)?(\([2-9]([02-9]\d|1[02-9])\)|[2-9]([02-9]\d|1[02-9]))-?[2-9]([02-9]\d|1[02-9])-?\d{4}$/);
  }, "Please specify a valid phone number");
} // end of function




// if the ajax call is successful, execute this function
// create the results table and populate it with the rates array
function searchSuccess(data, textStatus, jqXHR)
{
    // empty any rows that are present, if the user resubmits the form
 // $(document).ready(function() {


/*$("#myTable").on("load", "tr", function() {
    $("#pete").remove();

}); */

//var span123 = $('#myTable a').detach();

//$("#myTable tr a").detach();
//$("#myTable").find("tr:not(:first)").remove();

//var abc1234 = $('#myTable tr:last').after("<tr><td data-label='Rate' class = 'main-rate'>" + "123" + "%</td><td data-label='Apply' id = 'tree'><a href = '/contact'>Apply Now</a></td></tr>");

counter_z = 0;
$("#myTable").find('tr:not(:first)').remove();


//$("#myTable").find('tr').remove();


//var abc123 = $("#myTable").detach();


    $("#header_row").css("visibility","visible");


    // show error message if there are no programs available (inputs didn't meet investor adjustment requirements)
    if (data.length == 0)
    {
        $("#sorry").css("display","block");
        $("#resultsTable").css("display","none");
        $("#progressbar").css("display","none");
        $(".dashboard").css("display","none");

    }

    // there is a data input error
    else if (data == 0) {
      $("#sorry").css("display","block");
        $("#resultsTable").css("display","none");
        $("#progressbar").css("display","none");
        $(".dashboard").css("display","none");
    }

    // if there is at least one row of data (at least one program met investor guidelines)
    else if (data.length > 0)
    {   $("#sorry").css("display","none");
        $("#resultsTable").css("display","block");
       $(".dashboard").css("display","block");
	   console.log('VPRINT BEGINS');
console.log(data);
console.log('END');
        // data [rate, ysp, apr, payment, [title array breakdown - different per state], total title costs, adjustments, program name, closing costs to borrower]
        for (var i = 0; i < data.length; i++) {
            var convertedData = JSON.stringify(data); // data is returned from ajax call in JSON format; need to convert it
           // var table = document.getElementById("myTable");

    // build the Query string to pass data in the URL using JQuery's native param method

    /*
    data[i][0] = Rate
    data[i][1] = YSP
    data[i][2] = APR
    data[i][3] = Payment
    data[i][4] = Title Costs (array with the breakdown)
    data[i][5] = Total Title Costs (regardless of who pays it)
    data[i][6] = Adjustments
    data[i][7] = Program
    data[i][8] = Points
    data[i][9] = Closing Costs to the Borrower
    data[i][10] = Investor
    data[i][11] = Threshold YSP (amount we need to make to cover closing costs, etc.)

    MD Refi
    data[i][4][0] = Recording
    data[i][4][1] = Title Insurance
    data[i][4][2] = Abstract
    data[i][4][3] = Deed
    data[i][4][4] = Courier
    data[i][4][5] = Payoff
    data[i][4][6] = Settlement
    data[i][4][7] = Title Examination

    MD Purchase
    data[i][4][0] = Recording
    data[i][4][1] = Taxes
    data[i][4][2] = County Taxes
    data[i][4][3] = Purchase Taxes
    data[i][4][4] = Title Insurance
    data[i][4][5] = Abstract
    data[i][4][6] = Deed
    data[i][4][7] = Courier
    data[i][4][8] = Settlement
    data[i][4][9] = Title Examination
    data[i][4][10] = County Recording
    data[i][4][11] = County Tax



    */

      if ($('#id_loan_type').val() == 'refi_rate_term') {
        var nickname_loan_type = 'Refi: Rate & Term';
      }
      else if ($('#id_loan_type').val() == 'refi_cash_out') {
        var nickname_loan_type = 'Refi: Cash Out';
      }

      else {
        var nickname_loan_type = 'Purchase';
      }

      if ($('#id_property_type').val() == 'primary') {
        var nickname_property_type = 'Primary Residence';
      }
      else if ($('#id_property_type').val() == 'second') {
        var nickname_property_type = 'Second Home';
      }

      else {
        var nickname_property_type = 'Investment Property';
      }

      var params = {
        loan_type: nickname_loan_type,
        loan_balance: $('#id_loan_balance').val(),
        property_value: $('#id_property_value').val(),
        down_payment: $('#id_down_payment').val(),
        cash_out: $('#id_cash_out').val(),
        zip_code: $('#id_zip_code').val(),
        property_type: nickname_property_type,
        credit_score: $('#circles-slider').slider("value"),
        rate:data[i][0],
        y:data[i][1],
        apr:data[i][2],
        payment:data[i][3],
        title:data[i][5],
        //rate:data[i][6],
        program:data[i][7],
        points:data[i][8],
        cc:data[i][9],
        inv:data[i][10],
        county: user_county,
        state: user_state,
        loan_amount: guided_value
        //apr:data[i][11],

      };
        guided_value_formatted = parseFloat(guided_value);
        //test123 = guided_value.toFixed(3);
        guided_value_formatted = (guided_value_formatted).formatMoney(0, '.', ',');
         $( "#st" ).text(user_state);
         $( "#ct" ).text(user_county);
         $( "#la" ).text(guided_value_formatted);
      // $( "#pv" ).val($('#id_property_value').val());
       ltv = parseInt(guided_value) / parseInt($('#id_property_value').val());


$("#progressbar").css("display","block");
$( "#progressbar" ).progressbar( "value", ltv *100 );
$("#progressText").text((ltv *100).toFixed(1));
//("#progressbar").progressbar('value', obj.ltv * 100);


//var ex = "<a href = '/contact'>Apply Now</a>";

/*
if ($('#id_loan_type').val() == 'refi_rate_term') {
  test = 123;
//  var nickname_loan_type = 'Refi: Rate & Term';
}
else if ($('#id_loan_type').val() == 'refi_cash_out') {
test = 123;
  //var nickname_loan_type = 'Refi: Cash Out';
}\*/



      if (nickname_loan_type == 'Refi: Rate & Term' && user_state == 'maryland') {
        //county_tr = data[i][4][8]
      var recording_costs = data[i][4][0].formatMoney(2, '.', ',');
      var title_insurance = data[i][4][1].formatMoney(2, '.', ',');;
      var abstract = data[i][4][2].formatMoney(2, '.', ',');;
      var deed = data[i][4][3].formatMoney(2, '.', ',');;
      var courier = data[i][4][4].formatMoney(2, '.', ',');;
      var payoff = data[i][4][5].formatMoney(2, '.', ',');;
      var settlement = data[i][4][6].formatMoney(2, '.', ',');;
      var title_examination = data[i][4][7].formatMoney(2, '.', ',');;

  //  window.alert(title_costs);



        //var title_label_values = ["Recording Fees", "Title Insurance", "Abstract", "Deed", "Courier", "Payoff", "Settlement", "Title Examination"];
      //  var title_description = ["County Tax Rate of " + county_tr, "$4.68 per thousand up to $250K\,$4.44 per thousand up between $250K-$500K\,$4.08 per thousand up between $500K-$1000K\,$2.70 per thousand above $1000K  , ", "Abstract", "Deed", "Courier", "Payoff", "Settlement", "Title Examination"];
        // if (data[i][9]==0) {
        //   var refund_label="BFG Credit to Borrower";
        // }
      }
      else if (nickname_loan_type == 'Refi: Cash Out' && user_state == 'maryland') {
        var recording_costs = data[i][4][0].formatMoney(2, '.', ',');;
        var title_insurance = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var deed = data[i][4][3].formatMoney(2, '.', ',');;
        var courier = data[i][4][4].formatMoney(2, '.', ',');;
        var payoff = data[i][4][5].formatMoney(2, '.', ',');;
        var settlement = data[i][4][6].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][7].formatMoney(2, '.', ',');;
        //var title_label_values = ["Recording Fees", "Title Insurance", "Abstract", "Deed", "Courier", "Payoff", "Settlement", "Title Examination"];

      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland') {

        var recording_costs = data[i][4][0].formatMoney(2, '.', ',');;
        var md_county_transfer_tax = data[i][4][1].formatMoney(2, '.', ',');;
        var md_state_recordation_tax = data[i][4][2].formatMoney(2, '.', ',');;
        var title_insurance = data[i][4][3].formatMoney(2, '.', ',');;
        var abstract = data[i][4][4].formatMoney(2, '.', ',');;
        var deed = data[i][4][5].formatMoney(2, '.', ',');;
        var courier = data[i][4][6].formatMoney(2, '.', ',');;
        var settlement = data[i][4][7].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][8].formatMoney(2, '.', ',');;
        var md_county_tax_rate = data[i][4][9];;
		var county_recording_rate=data[i][4][9];;
		var county_tax_rate=data[i][4][10];;		
        //var title_label_values = ["Recording Fees", "County Transfer Tax", "State Recordation Tax", "Title Insurance", "Abstract", "Deed", "Courier", "Settlement", "Title Examination"];

      }
      else if (nickname_loan_type == 'Refi: Rate & Term' && user_state == 'virginia') {
        var va_trust_tax = data[i][4][0].formatMoney(2, '.', ',');;
        var title_insurance = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var courier = data[i][4][3].formatMoney(2, '.', ',');;
        var payoff = data[i][4][4].formatMoney(2, '.', ',');;
        var settlement = data[i][4][5].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][6].formatMoney(2, '.', ',');;
        //var title_label_values = ["Recording Fees", "Title Insurance", "Abstract", "Courier", "Payoff", "Settlement", "Title Examination"];

      }
      else if (nickname_loan_type == 'Refi: Cash Out' && user_state == 'virginia') {
        var va_trust_tax = data[i][4][0].formatMoney(2, '.', ',');;
        var title_insurance = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var courier = data[i][4][3].formatMoney(2, '.', ',');;
        var payoff = data[i][4][4].formatMoney(2, '.', ',');;
        var settlement = data[i][4][5].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][6].formatMoney(2, '.', ',');;
      //var title_label_values = ["Recording Fees", "Title Insurance", "Abstract", "Courier", "Payoff", "Settlement", "Title Examination"];
      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'virginia') {
        var va_deed_tax = data[i][4][0].formatMoney(2, '.', ',');;
        var va_trust_tax = data[i][4][1].formatMoney(2, '.', ',');;
        var title_costs = data[i][4][2].formatMoney(2, '.', ',');;
        var abstract = data[i][4][3].formatMoney(2, '.', ',');;
        var deed = data[i][4][4].formatMoney(2, '.', ',');;
        var courier = data[i][4][5].formatMoney(2, '.', ',');;
        var settlement = data[i][4][6].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][7].formatMoney(2, '.', ',');;
        //var title_label_values = ["Deed Tax", "Trust Tax", "Title Insurance", "Abstract", "Courier", "Payoff", "Settlement", "Title Examination"];

      }
      else if (nickname_loan_type == 'Refi: Rate & Term' && user_state == 'district of columbia') {
        var title_insurance = data[i][4][0].formatMoney(2, '.', ',');;
        var payoff = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var courier = data[i][4][3].formatMoney(2, '.', ',');;
        var settlement = data[i][4][4].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][5].formatMoney(2, '.', ',');;
        //var title_label_values = ["Title Insurance", "Payoff", "Abstract", "Courier", "Settlement", "Title Examination"];

      }
      else if (nickname_loan_type == 'Refi: Cash Out' && user_state == 'district of columbia') {

        var title_insurance = data[i][4][0].formatMoney(2, '.', ',');;
        var payoff = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var courier = data[i][4][3].formatMoney(2, '.', ',');;
        var settlement = data[i][4][4].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][4].formatMoney(2, '.', ',');;
        //var title_label_values = ["Title Insurance", "Payoff", "Abstract", "Courier", "Settlement", "Title Examination"];

      }
      else if (nickname_loan_type == 'Purchase' && user_state == 'district of columbia') {
        var dc_deed_recordation_tax = data[i][4][0].formatMoney(2, '.', ',');;
        var title_insurance = data[i][4][1].formatMoney(2, '.', ',');;
        var abstract = data[i][4][2].formatMoney(2, '.', ',');;
        var courier = data[i][4][3].formatMoney(2, '.', ',');;
        var deed = data[i][4][4].formatMoney(2, '.', ',');;
        var settlement = data[i][4][5].formatMoney(2, '.', ',');;
        var title_examination = data[i][4][6].formatMoney(2, '.', ',');;
      //  var title_label_values = ["Deed Recordation Tax", "Title Insurance", "Abstract", "Courier", "Deed", "Settlement", "Title Examination"];

      }


      //var myStringArray = ["Hello","World"];
      //var arrayLength = myStringArray.length;
      var total_true_cost = 0;
      for (var counter = 0; counter < data[i][4].length; counter++) {
        total_true_cost = total_true_cost + data[i][4][counter];
      //  total_trust_cost = total_trust_cost.formatMoney(2, '.', ',')
        }

      //logic to hide BFG credit div, named r12_1, r12_2, r12_3, r12_4, etc.
      counter_z = counter_z + 1;
      temp_id = 'r12_'+ counter_z;
	  
	  var property_value = $('#id_property_value').val();
var calculation_title='';
//Added by vprint
      if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type == 'Primary Residence' && property_value > 500000) {
        calculation_title='MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value up to $500,000 (The first $50,000 is exempt for owner-occupied properties).<br>The Montgomery County Recordation Tax is $10 per thousand for each thosand above $500,000 of the property value.';
          //$('#tooltip_message_1').replaceWith('d');

      }
      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type == 'Primary Residence' && property_value <=500000) {
        calculation_title='MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value (The first $50,000 is exempt for owner-occupied properties).';

      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type != 'Primary Residence' && property_value > 500000) {
        calculation_title='MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value oup to $500,000.<br>The Montgomery County Recordation Tax is $10 per thousand for each thosand above $500,000 of the property value.';
      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type != 'Primary Residence' && property_value <=500000) {
        calculation_title='MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand';
      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county!='Montgomery') {
        calculation_title='MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand';
      }
	  
	  var MarylandStateRecordationtax='Maryland State Recordation Tax';
	  var CountyTransfertax='County Transfer Tax';
	  var MarylandStateTransfertax='Maryland State Transfer Tax';
	  

if(user_state == 'maryland')
{
  if(user_county!='Montgomery' && nickname_loan_type == 'Purchase')
		{
		  MarylandStateRecordationtax= '$'+county_recording_rate +' per thousand loan amount. It is typical for the buyer and seller to split this cost (The amount shown is the buyer&#39;s portion, assuming a 50/50 split between buyer and seller)';
		}
  if(user_county!='Montgomery' && nickname_loan_type != 'Purchase')
  {
	MarylandStateRecordationtax= '$'+county_recording_rate +' per thousand on "new money" (new money is the loan amount which exceeds current loan balance)';
  }
  if(user_county=='Montgomery' && nickname_loan_type == 'Purchase')
  {
   if(property_value <=500000)
		 {
			MarylandStateRecordationtax= '$'+county_recording_rate +' per thousand purchase price.The first $50k is exempt if the property is owner occupied. (The amount shown is the buyer&#39;s portion, assuming a 50/50 split between buyer and seller)';
		 }
		 else if(property_value > 500000)
		 {
			MarylandStateRecordationtax= "$10 per thousand for each thousand purchase price.The first $50k is exempt if the property is owner occupied. (The amount shown is the buyer&#39;s portion, assuming a 50/50 split between buyer and seller)";
		 }
  }
  if(user_county=='Montgomery' && nickname_loan_type != 'Purchase')
  {
	if(property_value <=500000)
		 {
		  MarylandStateRecordationtax=  '$'+county_recording_rate +' per thousand on "new money"(new money is the loan amount which exceeds current loan balance).The first $50k is exempt if the property is owner occupied.';
		 }
		 else if(property_value > 500000)
		 {
		 MarylandStateRecordationtax= '$10 per thousand for each thousand on "new money"(new money is the loan amount which exceeds current loan balance).The first $50k is exempt if the property is owner occupied.'
		 }  
  }		
}
CountyTransfertax=county_tax_rate +'% of loan amount for ' +user_county+ ' County. (The amount shown is the buyer&#39;s portion, assuming a 50/50 split between buyer and seller)';
MarylandStateTransfertax= '.5% of loan amount for state of Maryland. The buyer is exempt from this tax if they are a first-time homebuyer. (The amount shown is the buyer&#39s portion, assuming a 50/50 split between buyer and seller)';

//var loan_amount=$('#la').html();
var loan_amount=guided_loan_amount;
var loanamount='LoanAmount';
  console.log("Testyutyutu   "+parseInt(loan_amount));
    console.log("Test  title_rates[0] "+title_rates[0]);
	console.log("Test  title_rates[1] "+title_rates[1]);
if (user_state == 'maryland' && nickname_loan_type== 'Purchase')
{
      if(loan_amount <= 250000){		
		loanamount="$"+title_rates[0][0] +" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[0][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[0][2]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[0][3]+" per thousand";
  }
}
else if (user_state == 'maryland' && nickname_loan_type != 'Purchase'){
  if(loan_amount <= 250000){
		loanamount="$"+title_rates[1][0]+" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[1][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[1][2]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[1][3]+" per thousand";
  }
}
else if (user_state == 'virginia' && nickname_loan_type == 'Purchase'){
      if(loan_amount <= 250000){
		loanamount="$"+title_rates[2][0]+" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[2][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[2][3]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[2][3]+" per thousand";
  }
}
else if (user_state == 'virginia' && nickname_loan_type != 'Purchase'){
      if(loan_amount <= 250000){
		loanamount="$"+title_rates[3][0]+" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[3][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[3][2]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[3][3]+" per thousand";
  }
}
else if (user_state == 'dc' && nickname_loan_type == 'Purchase'){
      if(loan_amount <= 250000){
		loanamount="$"+title_rates[4][0]+" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[4][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[4][2]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[4][3]+" per thousand";
  }
}
else if (user_state == 'dc' && nickname_loan_type != 'Purchase'){
      if(loan_amount <= 250000){
		loanamount="$"+title_rates[5][0]+" per thousand";
  }
  else if(loan_amount > 250000 && loan_amount <= 500000){
		loanamount="$"+title_rates[5][1]+" per thousand";
  }
  else if(loan_amount > 500000 && loan_amount <= 1000000){
		loanamount="$"+title_rates[5][2]+" per thousand";
  }
  else if(loan_amount > 1000000 && loan_amount <= 5000000){
		loanamount="$"+title_rates[5][3]+" per thousand";
  }
}
	  
/////
      var str = jQuery.param( params );
      $('#myTable tr:last').after(
        "<tr class = 'odd'>\
		  <td><i class='fa fa-angle-down rotate tooltip' style='color:#3498db'><span class='tooltiptext'>Click here for breakdown of costs</span></i></td>\
		    <td data-label='Rate' class = 'main-rate'>" + data[i][0].toFixed(3) + "%</td>\
            <td data-label='APR'>" + data[i][2].toFixed(3) + "%</td>\
            <td data-label='Payment'>$" + data[i][3].toFixed(2) + "</td>\
            <td data-label='Program'>" + data[i][7] + "</td>\
            <td data-label='Points'>" + data[i][8].toFixed(3)+ "</td>\
            <td data-label='Closing Costs' class = 'clickme'>$" + data[i][9].toFixed(2) + "</td>\
            <td data-label='Apply' id = 'tree'><a class = \'target\' href = \'https://www.blink.mortgage/app/signup/p/bfgusa\' target = \'_blank\'>Apply Now</a></td>\
        </tr>\
        <tr class = 'even'><td colspan = '8'>\
                  <h4>Breakdown of Title Costs</h4>\
                  <div class = 'r0'><div class = 'rlabel'><h6> State Recordation Tax <i class = 'tooltip2 fa fa-question-circle fa-1x' title='"+MarylandStateRecordationtax+"'></i></h6></div><div class = 'rvalue'><p>$" + recording_costs + "</p></div></div>\
                  <div class = 'r1'><div class = 'rlabel'><h6> County Recordation Tax <i class = 'tooltip2 fa fa-question-circle fa-1x' title='"+CountyTransfertax+"'></i></h6></div><div class = 'rvalue'><p>$" +  md_county_transfer_tax + "</p></div></div>\
                  <div class = 'r2'><div class = 'rlabel'><h6> State Transfer Tax <i class='tooltip2 fa fa-question-circle fa-1x' title='"+MarylandStateTransfertax+"'></i></h6></div><div class = 'rvalue'><p>$" + md_state_recordation_tax + "</p></div></div>\
                  <div class = 'r3'><div class = 'rlabel'><h6>Title Insurance<i class = 'tooltip2 fa fa-question-circle fa-1x' title='"+loanamount+"'></i></h6></div><div class = 'rvalue'><p>$" + title_insurance + "</p></div></div>\
                  <div class = 'r4'><div class = 'rlabel'><h6>Abstract</h6></div><div class = 'rvalue'><p>$" + abstract + "</p></div></div>\
                  <div class = 'r5'><div class = 'rlabel'><h6>Deed</h6></div><div class = 'rvalue'><p>$" + deed + "</p></div></div>\
                  <div class = 'r6'><div class = 'rlabel'><h6>Courier</h6></div><div class = 'rvalue'><p>$" + courier + "</p></div></div>\
                  <div class = 'r7'><div class = 'rlabel'><h6>Title Examination</h6></div><div class = 'rvalue'><p>$" + title_examination + "</p></div></div>\
                  <div class = 'r8'><div class = 'rlabel'><h6>Payoff</h6></div><div class = 'rvalue'><p>$" + payoff + "</p></div></div>\
                  <div class = 'r9'><div class = 'rlabel'><h6>VA Deed Tax</h6></div><div class = 'rvalue'><p>$" + va_deed_tax + "</p></div></div>\
                  <div class = 'r10'><div class = 'rlabel'><h6>VA Trust Tax</h6></div><div class = 'rvalue'><p>$" + va_trust_tax + "</p></div></div>\
                  <div class = 'r11'><div class = 'rlabel'><h6>DC Deed Recordation Tax</h6></div><div class = 'rvalue'><p>$" + dc_deed_recordation_tax + "</p></div></div>\
                  <div id = " + temp_id + "><div class = 'rlabel'><h6>BFG Credit</h6></div><div class = 'rvalue'><p>-$" + total_true_cost.formatMoney(2, '.', ',') + "</p></div></div>\
        </td></tr>");

        // <div class = 'r1'><div class = 'rlabel'><h6>MD County Recordation Tax <i class = 'tooltip2 fa fa-question-circle fa-1x' data-tooltip-content='.tooltip_message_1'></i></h6></div><div class = 'rvalue'><p>$" +  md_county_transfer_tax + "</p></div></div>\
        // <div class = 'r2'><div class = 'rlabel'><h6>MD State Transfer Tax <i class='tooltip2 fa fa-question-circle fa-1x' title='.tooltip_message_2'></i></h6></div><div class = 'rvalue'><p>$" + md_state_recordation_tax + "</p></div></div>\

        // Adapted from http://www.jankoatwarpspeed.com/expand-table-rows-with-jquery-jexpand-plugin/
        // Expanable table rows to show title breakdown
       //$("#myTable tr:not(.odd)").hide();

      // window.alert(abstract)

    //  $('#county_value').val(user_county); // this if for injecting the value in the html tooltip in the rates page

/*
      var property_value = $('#id_property_value').val();

      if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type == 'Primary Residence' && property_value > 500000) {
        $('.tooltip_message_1').html('MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value up to $500,000 (The first $50,000 is exempt for owner-occupied properties).<br>The Montgomery County Recordation Tax is $10 per thousand for each thosand above $500,000 of the property value.');
          //$('#tooltip_message_1').replaceWith('d');

      }
      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type == 'Primary Residence' && property_value <=500000) {
        $('.tooltip_message_1').html('MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value (The first $50,000 is exempt for owner-occupied properties).');

      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type != 'Primary Residence' && property_value > 500000) {
        $('.tooltip_message_1').html('MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand of the property value oup to $500,000.<br>The Montgomery County Recordation Tax is $10 per thousand for each thosand above $500,000 of the property value.');
      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county=='Montgomery' && nickname_property_type != 'Primary Residence' && property_value <=500000) {
        $('.tooltip_message_1').html('MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand');
      }

      else if (nickname_loan_type == 'Purchase' && user_state == 'maryland' && user_county!='Montgomery') {
        $('.tooltip_message_1').html('MD '+ user_county + ' County Recordation Tax is $' + md_county_tax_rate + ' per thousand');
      }

*/


  //  $('#tooltip_data_county_rate').html(md_county_tax_rate);



       $("#myTable").find("tr:first-child").show();
       $(".even").hide();
	    console.log("VPRINT RESHMA111")
       //$("#myTable tr:not(.odd)").hide();
         $("#myTable tr:last").prev().click(function(){
             $(this).next("tr").toggle();
			 
             //$(this).find(".arrow").toggleClass("up");
			 //$(this).find(".rotate").toggleClass("down");
			 //.find(".tooltiptext").toggleClass("hidetext");
			
			 
			 
         });




         if (typeof(recording_costs) == 'undefined' || recording_costs=='0.00') {
            $('.r0').hide();
          }
        if (typeof(md_county_transfer_tax) == 'undefined' || md_county_transfer_tax=='0.00') {
          $('.r1').hide();
        }
        if (typeof(md_state_recordation_tax) == 'undefined' || md_state_recordation_tax=='0.00') {
          $('.r2').hide();
        }
        if (typeof(title_insurance) == 'undefined' || title_insurance=='0.00') {
          $('.r3').hide();
        }

        if (typeof(abstract) == 'undefined' || abstract=='0.00') {
          $('.r4').hide();

        }

        if (typeof(deed) == 'undefined' || deed=='0.00') {
          $('.r5').hide();
        }
        if (typeof(courier) == 'undefined' || courier=='0.00') {
          $('.r6').hide();
        }
        if (typeof(title_examination) == 'undefined' || title_examination=='0.00') {
          $('.r7').hide();
        }
        if (typeof(payoff) == 'undefined' || payoff=='0.00') {
          $('.r8').hide();
        }
        if (typeof(va_deed_tax) == 'undefined' || va_deed_tax=='0.00') {
           $('.r9').hide();
         }
        if (typeof(va_trust_tax) == 'undefined' || va_trust_tax=='0.00') {
          $('.r10').hide();
        }
        if (typeof(dc_deed_recordation_tax) == 'undefined' || dc_deed_recordation_tax=='0.00') {
          $('.r11').hide();
        }

        if (data[i][9] > 0) {
            $('#'+temp_id).hide()
        }
      //  window.alert(typeof(title_insurance));


        //  window.alert( $("tr.even:nth-child(5)").data   );

          //$(tr.even:nth-child(11)
        //$(tr.even:nth-child(11))





        // if (sum(data[i][4]) > 0) {
        //   $('.r12').hide();
        // }




        //windows.console (data[i][9])
          //$('.title0').hide();

         //window.alert(typeof(data[i][4][1]));
          //if (data[i][4][10] == 0 || data[i][4][10] == 'undefined') {

          // for (x = 0; x <= data[i][4].length; x++) {
          //   var title_name = 'title';
          //   var title_name2 = title_name.concat(i);
          //   //window.alert(title_name2)
          //   if (typeof(data[i][4][x]) != 'number' || data[i][4][0]==0) {
          //   //   $('#title9').hide();
          //   $('.'+title_name2).hide();
          // }
          //
          //   }


          // if (typeof(data[i][4][10]) != 'number') {
          //   $('#title10').hide();
          //   window.alert(data[i][4].length)
          //
          // }
          //
          // if (typeof(data[i][4][9]) != 'number') {
          //   $('#title9').hide();
          //
          // }
          //
          // if (typeof(data[i][4][11]) != 'number') {
          //   $('#title11').hide();
          //
          // }




            //  $('#show').click(function(){
            //      $('testme').hide();
            //  });

            //  $('tr.header').click(function(){
            //     $(this).nextUntil('tr.header').css('display', function(i,v){
            //       return this.style.display === 'table-row' ? 'none' : 'table-row';
            //       });
            //     });

    //$('#myTable tr:last').append(abc123);

    // $(abc123).appendTo('#myTable tr:last');

/*     else {

     }*/
      //  $('#myTable tr:last').appendTo(abc123);

     //  span123.appendTo('#myTable td#tree2');

       //                 <td data-label='Apply'><a class = \'target\' href = \'/application\/?"+str+"'>Apply Now</a></td>\


 /*   $("button").click(function(){
        alert('yup');
    });*/

       // since the links are created dynamically after page load, you need to register the event using the "on" method
       // http://stackoverflow.com/questions/6658752/jquery-click-event-doesnt-work-on-dynamically-generated-elements

        }
    } // end of If Empty Data

   //});   // );
}


function failure(){
    alert("failure");

}



function zc_lookup(){
  //$("input").inputmask('remove');

  var zip_flag = 0;
  var zip_message = document.getElementById("zcode");

  if ($('#id_zip_code').val().length >= 1) {
    //var zip_flag = 0;
    $.ajax({
      type: "GET",
    // async: false,
      url: "/zip_test/",
      data: {
          'zc_check' : $('#id_zip_code').val()
      },
      success: function(data) {

        // data is in the following format: a dictionary inside an array inside an array
        // [1, [{"county": "Montgomery"}], [{"state": "maryland"}]]

          if (data[0] == 1) {

              user_county = data[1][0].county;
              user_state = data[2][0].state;

              /*if (data[1][0].county == 'Montgomery') {
                  alert("yay");
              }*/

           // alert (data[1]);
			if(user_state=='Maryland' || user_state=='maryland'){
			$('.first_time_homebuyer').show();
			}
			else{
			$('.first_time_homebuyer').hide();
			}
            zip_message.style.display = 'none';

            field_checks(); // since AJAX is asyncronous, we want to wait for the value to be retured before proceeding; otherwise, the function will continue executing without the returned value

          }

          else  {


            zip_message.style.display = 'block';
            searchSuccess(0); // call the searchSuccess function and display the error message to the user



          }
          //alert (data);
          /*if (data==1) {
            alert("match: " + data);
            zip_flag = data;
          }*/
      },

      error : function(xhr,errmsg,err) {
          alert ("error: " + xhr.status + " " + errmsg + " " + err);
      },

      dataType: 'json',
    }); // end of ajax function
    //alert ("data is : " + zip_flag);
    //zip_flag = 1;

  } // end of IF


  return zip_flag;
}


function val_Rules () {

  if ($('#id_cash_out').val() == '') {
    $('#id_cash_out').val(0);
  }

  var validation_flag = 0; // 0 = there are no errors
  var validation1 = document.getElementById("validation1");
  var validation2 = document.getElementById("validation2");
  var validation3 = document.getElementById("validation3");
  var validation4 = document.getElementById("validation4");
  var validation5 = document.getElementById("validation5");
  var validation6 = document.getElementById("validation6");
  var validation7 = document.getElementById("validation7");
  var validation8 = document.getElementById("validation8");
  validation1.style.display = "none";
  validation2.style.display = "none";
  validation3.style.display = "none";
  validation4.style.display = "none";
  validation5.style.display = "none";
  validation6.style.display = "none";
  validation7.style.display = "none";
  validation8.style.display = "none";

  var minLoanAmount = 100000;


 //if ($('#id_property_value').val() < 50000 ){
  if ($('#id_loan_type').val() == 'refi_rate_term') {


      if ($('#id_loan_balance').val() < minLoanAmount) {
        validation2.style.display = "block";
        validation_flag = 1;

        //searchSuccess(0);
      }

      if ($('#id_property_value').val() < minLoanAmount ) {
        validation1.style.display = "block";
        validation_flag = 1;
        //searchSuccess(0);
      }

      if (parseInt($('#id_loan_balance').val())  > parseInt($('#id_property_value').val())) {
        validation3.style.display = "block";
        validation_flag = 1;
      }

  }

  else if ($('#id_loan_type').val() == 'refi_cash_out') {


    if (  parseInt(    $('#id_loan_balance').val()  ) + parseInt(  $('#id_cash_out').val())  < minLoanAmount ) {
      validation4.style.display = "block";
      validation_flag = 1;
    }

    if (  parseInt(   $('#id_property_value').val()   ) < parseInt(  $('#id_loan_balance').val()  ) + parseInt(  $('#id_cash_out').val()  )) {
      validation5.style.display = "block";
      validation_flag = 1;
    }

    if ( parseInt(  $('#id_loan_balance').val()  ) < parseInt(  $('#id_cash_out').val() ) ) {
      validation8.style.display = "block";
      validation_flag = 1;
    }

    if (parseInt($('#id_cash_out').val()) == 0 ) {
      validation6.style.display = "block";
      validation_flag = 1;
    }
  }

  else {

     if (  parseInt(  $('#id_property_value').val()  ) - parseInt($('#id_down_payment').val())  < minLoanAmount ) {
      validation7.style.display = "block";
      validation_flag = 1;
    }

  }

  return validation_flag;
}

// called when zc_lookup succeeds
function field_checks (){


validation_flag = val_Rules(); // call the validations

if (validation_flag == 1) {
  searchSuccess(0);
 // $("#perf").css("display","none");
}
else {

  var dp;
  //var derived_loan_amount;
  var lb;
  var co;

  if ($('#id_loan_type').val() == 'refi_cash_out') {
       co = $('#id_cash_out').val();
      /* if (co == ''){
        co = 0;
      }*/
     // derived_loan_amount = parseInt($('#id_loan_balance').val()) + parseInt($('#id_cash_out').val());
      //derived_loan_amount = parseInt($('#id_loan_balance').val()) + parseInt(co);
      dp = 0;
      lb = $('#id_loan_balance').val();

  }

  else if ($('#id_loan_type').val() == 'refi_rate_term') {
      //derived_loan_amount = $('#id_loan_balance').val();
      dp = 0;
      lb = $('#id_loan_balance').val();
      co = 0;


  // purchase
  } else {
      //var value5 = parseInt($("#id_property_value").val()) - parseInt($("#id_down_payment").val());

      //derived_loan_amount = parseInt($("#id_property_value").val()) - parseInt($("#id_down_payment").val());
     // derived_loan_amount = parseInt($("#id_property_value").val()) - parseInt($("#id_down_payment").val());
      dp = $('#id_down_payment').val();
      lb = 0;
      co = 0;

  }

    var zc = $('#id_zip_code').val();

       //debugger;

    // url parameter is the index, thus a blank value
    // if ajax call succeeds, call the "searchSuccess" function

    // when you "refresh" the page, loan_amount receives " $250,000". this is a workaround to fix this

    // workaround to fix the bug that results from hitting refresh on the browser. "guided value" is sent to server as "$ 250,000"
    if (typeof guided_value == 'string') {
      guided_value = guided_value.replace(/\D/g,'');
    }

    $.ajax({
        type: "POST",
        //async: false,
        url: "",
        data: {
           loan_type : $('#id_loan_type').val(),
            loan_balance : $('#id_loan_balance').val(),


            //loan_amount : derived_loan_amount,
            loan_amount : guided_value,
            //loan_amount: val5,

            //property_value : $('#id_property_value').val().replace(/,/g, ''),
            property_value : $('#id_property_value').val(),
           // property_value : $('#id_property_value').val(),
            zip_code : $('#id_zip_code').val(),
            //credit_score : $('#id_credit_score').val(),
            credit_score: $('#circles-slider').slider("value"),
            property_type: $('#id_property_type').val(),
            down_payment: dp,
            cash_out: co

        },
        success: searchSuccess,

        //error: failure(),
        dataType: 'json'
    }); // end of ajax function
  } // end of If statement

  /*else {
    if ($('#id_property_value').val() <= 65000) {
      var abcd = getElementById("tester");
      abcd.style.display = block;
    }
  }*/

}

/*
// From Stack Overflow: http://stackoverflow.com/questions/995183/how-to-allow-only-numeric-0-9-in-html-inputbox-using-jquery/6240876#6240876
// Values 110 and 190 taken out of original Stack Overflow post, to prevent users from entering a decimal point.
function keypress_validation() {
  $("input").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right, down, up
            (e.keyCode >= 35 && e.keyCode <= 40)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
}
*/


// From Stack Overflow, to format currency
// http://stackoverflow.com/questions/149055/how-can-i-format-numbers-as-money-in-javascript
Number.prototype.formatMoney = function(c, d, t){
var n = this,
    c = isNaN(c = Math.abs(c)) ? 2 : c,
    d = d == undefined ? "." : d,
    t = t == undefined ? "," : t,
    s = n < 0 ? "-" : "",
    i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
   return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
 };


function paymentCalculation() {

  // this the currency mask. it applies the formatting when the user enters a value

    //if ($('#id_loan_amount_calculator').val() > 0 && $('#id_loan_amount_calculator').val() <= 3000000  && $('#id_interest_rate').val() > 0 && $('#id_interest_rate').val() <= 20  && $('#id_months').val() >=12 && $('#id_months').val() <=480) {
   if ($('#id_loan_amount_calculator').val() > 0 && $('#id_loan_amount_calculator').val() <= 3000000 ) {
   /* var x = $('#id_interest_rate').val();
    if (x >=1 && x <= 20) {
        x = x / 100;
    }*/

   /* if ($('#id_interest_rate').val()=='') {
      $('#id_interest_rate').val() = 1;
    }*/

    var IR = $('#id_interest_rate').val()/100;
    var loanMonths = parseInt($('#id_months').val()) * 12;
    //var IR = $('#id_interest_rate').val()/100;
   // var IR = .07;
    if (IR > 0) {

    // url parameter is the index, thus a blank value
    // if ajax call succeeds, call the "searchSuccess" function
    $.ajax({
        type: "POST",
        url: "/calculator/",
        data: {
            loan_amount_calculator : $('#id_loan_amount_calculator').val(),
            interest_rate : IR,
            //interest_rate : $('#id_interest_rate').val(),
            months : loanMonths
        },
        success: calculatorSuccess,
        error : function(xhr,errmsg,err) {
            alert ("error: " + xhr.status + " " + errmsg + " " + err);
        },
        //error: failure,
        dataType: 'json'
    }); // end of ajax function
  } // en dof IF
  } // end of If statement
}

function calculatorSuccess(data, textStatus, jqXHR)
{
    //$(document).ready(function() {
      //$("#amortization_table").find('tr:not(:first)').remove();

      $("#payment").css("visibility","visible");
     //$("#payment_amount").text(data[0][0].formatMoney(2, '.', ','));
      $("#payment_amount").text('$' + data.formatMoney(2, '.', ','));
     // $("#first_row").css("visibility","visible");

      /*for (var i = 0; i < data.length; i++) {
            var convertedData = JSON.stringify(data); // data is returned from ajax call in JSON format; need to convert it
            var table = document.getElementById("amortization_table");
            var row = table.insertRow(i+1);
            //var temp = "rowDetails(" + convertedData + "," + i + ")";
            //row.setAttribute("onclick", temp); // dynamically create the "onclick" attribute for each row in the table
            //row.setAttribute("onmouseover", "change_color()");

            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            var cell7 = row.insertCell(6);
            var cell8 = row.insertCell(7);


            cell1.setAttribute("class","rate_cell");
            cell2.setAttribute("class","apr_cell");
            cell3.setAttribute("class","payment_cell");
            cell4.setAttribute("class","program_cell");


            cell1.innerHTML = i+1; // payment
            cell2.innerHTML = '$' + (data[i][0]).formatMoney(2, '.', ','); // payment
            cell3.innerHTML = '$' + (data[i][1]).formatMoney(2, '.', ','); // balance
            cell4.innerHTML = '$' + (data[i][2]).formatMoney(2, '.', ',');// interest
            cell5.innerHTML = '$' + (data[i][4]).formatMoney(2, '.', ','); // principle
            cell6.innerHTML = '$' + (data[i][3]).formatMoney(2, '.', ','); // total interest
            cell7.innerHTML = '$' + (data[i][5]).formatMoney(2, '.', ','); // total principle
            cell8.innerHTML = '$' + (data[i][6]).formatMoney(2, '.', ','); // total paid

        }
        var total_interest_payment = (data[data.length-1][3]).formatMoney(2, '.', ',');
        $("#total_interest_bill").html(total_interest_payment);

        var total_payment = (data[data.length-1][6]).formatMoney(2, '.', ',');
        $("#total_bill").html(total_payment); */


    //});

}


// http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
function getParameterByName(name) {
                name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
                var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
                results = regex.exec(location.search);
                return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
            }
/*function calculatorSuccess(data, textStatus, jqXHR)
{
    //$(document).ready(function() {
      $("#amortization_table").find('tr:not(:first)').remove();

      $("#payment").css("visibility","visible");
     //$("#payment_amount").text(data[0][0].formatMoney(2, '.', ','));
      $("#payment_amount").text('$' + data[0][0].formatMoney(2, '.', ','));
      $("#first_row").css("visibility","visible");

      for (var i = 0; i < data.length; i++) {
            var convertedData = JSON.stringify(data); // data is returned from ajax call in JSON format; need to convert it
            var table = document.getElementById("amortization_table");
            var row = table.insertRow(i+1);
            //var temp = "rowDetails(" + convertedData + "," + i + ")";
            //row.setAttribute("onclick", temp); // dynamically create the "onclick" attribute for each row in the table
            //row.setAttribute("onmouseover", "change_color()");

            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            var cell7 = row.insertCell(6);
            var cell8 = row.insertCell(7);


            cell1.setAttribute("class","rate_cell");
            cell2.setAttribute("class","apr_cell");
            cell3.setAttribute("class","payment_cell");
            cell4.setAttribute("class","program_cell");


            cell1.innerHTML = i+1; // payment
            cell2.innerHTML = '$' + (data[i][0]).formatMoney(2, '.', ','); // payment
            cell3.innerHTML = '$' + (data[i][1]).formatMoney(2, '.', ','); // balance
            cell4.innerHTML = '$' + (data[i][2]).formatMoney(2, '.', ',');// interest
            cell5.innerHTML = '$' + (data[i][4]).formatMoney(2, '.', ','); // principle
            cell6.innerHTML = '$' + (data[i][3]).formatMoney(2, '.', ','); // total interest
            cell7.innerHTML = '$' + (data[i][5]).formatMoney(2, '.', ','); // total principle
            cell8.innerHTML = '$' + (data[i][6]).formatMoney(2, '.', ','); // total paid

        }
        var total_interest_payment = (data[data.length-1][3]).formatMoney(2, '.', ',');
        $("#total_interest_bill").html(total_interest_payment);

        var total_payment = (data[data.length-1][6]).formatMoney(2, '.', ',');
        $("#total_bill").html(total_payment);


    //});

}*/
