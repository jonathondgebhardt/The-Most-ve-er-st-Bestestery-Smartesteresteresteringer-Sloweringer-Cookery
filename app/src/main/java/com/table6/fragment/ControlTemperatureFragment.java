package com.table6.fragment;

import android.content.Context;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.TextInputEditText;
import android.support.v4.app.Fragment;
import android.text.InputType;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.table6.activity.R;

public class ControlTemperatureFragment extends Fragment {

    private Button controlTemperatureBtn;
    private TextInputEditText controlTemperatureTxt;
    private OnControlTemperatureFragmentInteractionListener mListener;

    public ControlTemperatureFragment() {
        // Required empty public constructor
    }

    public static ControlTemperatureFragment newInstance() {
        ControlTemperatureFragment fragment = new ControlTemperatureFragment();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_control_temperature, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        controlTemperatureTxt = (TextInputEditText) view.findViewById(R.id.controlTemperatureTxt);
        controlTemperatureTxt.setInputType(InputType.TYPE_CLASS_NUMBER);
        controlTemperatureTxt.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                String newTemperature = controlTemperatureTxt.getText().toString();

                if (actionId == EditorInfo.IME_ACTION_DONE && !newTemperature.isEmpty()) {
                    mListener.onControlTemperatureFragmentInteraction(newTemperature);
                    Toast.makeText(getActivity(), "Setting temperature to " + newTemperature, Toast.LENGTH_LONG ).show();
                }

                return false;
            }
        });

        controlTemperatureBtn = (Button) view.findViewById(R.id.controlTemperatureBtn);
        controlTemperatureBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String newTemperature = controlTemperatureTxt.getText().toString();
                if(!newTemperature.isEmpty()) {
                    mListener.onControlTemperatureFragmentInteraction(newTemperature);
                    Toast.makeText(getActivity(), "Setting temperature to " + newTemperature, Toast.LENGTH_LONG ).show();
                }
            }
        });
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnControlTemperatureFragmentInteractionListener) {
            mListener = (OnControlTemperatureFragmentInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    public interface OnControlTemperatureFragmentInteractionListener {
        void onControlTemperatureFragmentInteraction(String x);
    }
}
